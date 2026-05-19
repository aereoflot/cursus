
import re
import sys
from typing import Dict, List, Optional, Set, Tuple


class ParseError(Exception):
    """Exception raised for errors during map file parsing."""
    pass


class Zone:
    """Represents a zone/node in the map.

    Attributes:
        name: Unique identifier for the zone.
        x: X coordinate of the zone.
        y: Y coordinate of the zone.
        is_start: Whether this zone is a start hub.
        is_end: Whether this zone is an end hub.
        zone_type: Type of zone (normal, blocked, restricted, priority).
        color: Optional ANSI color name for visualization.
        max_drones: Maximum number of drones that can occupy this zone.
    """

    def __init__(self, name: str, x: int, y: int,
                 is_start: bool = False, is_end: bool = False,
                 zone_type: str = "normal", color: Optional[str] = None,
                 max_drones: int = 1):
        """Initialize a Zone instance.

        Args:
            name: Unique identifier for the zone.
            x: X coordinate of the zone.
            y: Y coordinate of the zone.
            is_start: Whether this zone is a start hub. Defaults to False.
            is_end: Whether this zone is an end hub. Defaults to False.
            zone_type: Type of zone. Defaults to "normal".
            color: Optional color name for visualization. Defaults to None.
            max_drones: Maximum number of drones allowed. Defaults to 1.
        """

        self.name = name
        self.x = x
        self.y = y
        self.is_start = is_start
        self.is_end = is_end
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones


class Connection:
    """Represents a connection/edge between two zones.

    Attributes:
        zone1: Name of the first zone.
        zone2: Name of the second zone.
        max_link_capacity: Maximum number of
            drones that can traverse this connection simultaneously.
    """

    def __init__(self, zone1: str, zone2: str,
                 max_link_capacity: int = 1):
        """Initialize a Connection instance.

        Args:
            zone1: Name of the first connected zone.
            zone2: Name of the second connected zone.
            max_link_capacity: Maximum capacity of the connection.
                Defaults to 1.
        """
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity


class MapData:
    """Container for parsed map data.

    Attributes:
        nb_drones: Number of drones in the scenario.
        zones: Dictionary mapping zone names to Zone objects.
        connections: List of Connection objects.
        start_hub: Name of the starting zone.
        end_hub: Name of the destination zone.
    """

    def __init__(self) -> None:
        """Initialize a MapData instance with empty data."""
        self.nb_drones: int = 0
        self.zones: Dict[str, Zone] = {}
        self.connections: List[Connection] = []
        self.start_hub: Optional[str] = None
        self.end_hub: Optional[str] = None


class Parser:
    """Parser for map configuration files.

    This parser reads and validates map files containing zone and
    connection definitions. It ensures data consistency and raises
    ParseError for invalid input.

    Attributes:
        VALID_ZONE_TYPES: Set of valid zone type values.
        filepath: Path to the map file to parse.
        data: Parsed map data container.
        _parsed_connections: Set of parsed connection pairs to detect
            duplicates.
        _nb_drones_found: Flag indicating if nb_drones has been parsed.
    """

    VALID_ZONE_TYPES = {"normal", "blocked", "restricted", "priority"}

    def __init__(self, filepath: str):
        """Initialize a Parser instance.

        Args:
            filepath: Path to the map file to parse.
        """
        self.filepath = filepath
        self.data = MapData()
        self._parsed_connections: Set[Tuple[str, str]] = set()
        self._nb_drones_found = False

    def parse(self) -> MapData:
        """Parse the map file and return validated map data.

        Returns:
            MapData: The parsed map data.

        Raises:
            ParseError: If the file is not found or contains
                invalid data.
        """
        try:
            with open(self.filepath, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    self._parse_line(line, line_number)
        except FileNotFoundError:
            raise ParseError(f"Error: File '{self.filepath}' not found.")

        self._validate_final_state()
        return self.data

    def _parse_line(self, line: str, line_number: int) -> None:
        """Parse a single line from the map file.

        Args:
            line: The line to parse.
            line_number: The line number for error reporting.

        Raises:
            ParseError: If the line contains invalid syntax or data.
        """
        clean_line = line.split('#')[0].strip()
        if not clean_line:
            return

        if ':' not in clean_line:
            raise ParseError(
                f"Line {line_number}: Invalid syntax, missing colon. "
                f"'{clean_line}'"
            )

        prefix, rest = [part.strip() for part in clean_line.split(':', 1)]

        if prefix == 'nb_drones':
            self._parse_nb_drones(rest, line_number)
        elif prefix in ('start_hub', 'end_hub', 'hub'):
            if not self._nb_drones_found:
                raise ParseError(
                    f"Line {line_number}: 'nb_drones' must be "
                    "defined before zones."
                )
            self._parse_zone(prefix, rest, line_number)
        elif prefix == 'connection':
            if not self._nb_drones_found:
                raise ParseError(
                    f"Line {line_number}: 'nb_drones' must be "
                    "defined before connections."
                )
            self._parse_connection(rest, line_number)
        else:
            raise ParseError(f"Line {line_number}: Unknown prefix '{prefix}'.")

    def _extract_metadata(self, text: str,
                          line_number: int) -> Tuple[str, Dict[str, str]]:
        """Extract metadata from bracketed text.

        Args:
            text: The text containing metadata in brackets.
            line_number: The line number for error reporting.

        Returns:
            Tuple[str, Dict[str, str]]: The remaining text and
                metadata dictionary.

        Raises:
            ParseError: If metadata syntax is invalid.
        """
        metadata = {}
        rest_text = text

        match = re.search(r'\[(.*?)\]', text)
        if match:
            meta_str = match.group(1)
            rest_text = (text[:match.start()].strip() + " " +
                         text[match.end():].strip())

            items = meta_str.split()
            for item in items:
                if '=' not in item:
                    raise ParseError(
                        f"Line {line_number}: Invalid metadata "
                        f"syntax '{item}'. Expected key=value."
                    )
                key, value = item.split('=', 1)
                metadata[key] = value

        return rest_text.strip(), metadata

    def _parse_nb_drones(self, value_str: str,
                         line_number: int) -> None:
        """Parse the number of drones.

        Args:
            value_str: String representation of the number of drones.
            line_number: The line number for error reporting.

        Raises:
            ParseError: If the value is not a positive integer or
                already defined.
        """
        if self._nb_drones_found:
            raise ParseError(
                f"Line {line_number}: 'nb_drones' is already defined."
            )
        try:
            val = int(value_str)
            if val <= 0:
                raise ValueError()
            self.data.nb_drones = val
            self._nb_drones_found = True
        except ValueError:
            raise ParseError(
                f"Line {line_number}: 'nb_drones' must be "
                "a positive integer."
            )

    def _parse_zone(self, prefix: str, rest: str,
                    line_number: int) -> None:
        """Parse a zone definition.

        Args:
            prefix: The zone type prefix (start_hub, end_hub, or hub).
            rest: The zone definition text.
            line_number: The line number for error reporting.

        Raises:
            ParseError: If zone data is invalid or duplicated.
        """
        rest_text, metadata = self._extract_metadata(rest, line_number)
        parts = rest_text.split()

        if len(parts) != 3:
            raise ParseError(
                f"Line {line_number}: Zone must have name, x, y. "
                f"Found '{rest_text}'."
            )

        name, x_str, y_str = parts

        if '-' in name or ' ' in name:
            raise ParseError(
                f"Line {line_number}: Zone name '{name}' contains "
                "invalid characters (dashes or spaces)."
            )
        if name in self.data.zones:
            raise ParseError(
                f"Line {line_number}: Zone '{name}' is "
                "already defined."
            )

        try:
            x, y = int(x_str), int(y_str)
        except ValueError:
            raise ParseError(
                f"Line {line_number}: Coordinates for zone '{name}' "
                "must be integers."
            )

        is_start = prefix == 'start_hub'
        is_end = prefix == 'end_hub'

        if is_start:
            if self.data.start_hub:
                raise ParseError(
                    f"Line {line_number}: Multiple 'start_hub' "
                    "definitions found."
                    )
            self.data.start_hub = name
        if is_end:
            if self.data.end_hub:
                raise ParseError(
                    f"Line {line_number}: Multiple 'end_hub' "
                    "definitions found."
                    )
            self.data.end_hub = name

        zone_type = metadata.get('zone', 'normal')
        if zone_type not in self.VALID_ZONE_TYPES:
            raise ParseError(
                f"Line {line_number}: Invalid zone type "
                f"'{zone_type}'."
            )

        color = metadata.get('color')

        max_drones = 1
        if 'max_drones' in metadata:
            try:
                max_drones = int(metadata['max_drones'])
                if max_drones <= 0:
                    raise ValueError()
            except ValueError:
                raise ParseError(
                    f"Line {line_number}: 'max_drones' must be "
                    "a positive integer."
                    )

        self.data.zones[name] = Zone(
            name, x, y, is_start, is_end, zone_type, color, max_drones
            )

    def _parse_connection(self, rest: str,
                          line_number: int) -> None:
        """Parse a connection definition.

        Args:
            rest: The connection definition text.
            line_number: The line number for error reporting.

        Raises:
            ParseError: If connection data is invalid or duplicated.
        """
        rest_text, metadata = self._extract_metadata(rest, line_number)

        parts = rest_text.split('-')
        if len(parts) != 2:
            raise ParseError(
                f"Line {line_number}: Connection must be formatted as "
                "'zone1-zone2'.")

        z1, z2 = parts[0].strip(), parts[1].strip()

        if z1 not in self.data.zones:
            raise ParseError(
                f"Line {line_number}: Unknown zone '{z1}' "
                "in connection."
            )
        if z2 not in self.data.zones:
            raise ParseError(
                f"Line {line_number}: Unknown zone '{z2}' "
                "in connection."
            )

        edge_key1 = (z1, z2)
        edge_key2 = (z2, z1)
        if edge_key1 in self._parsed_connections or \
           edge_key2 in self._parsed_connections:
            raise ParseError(
                f"Line {line_number}: Duplicate connection "
                f"between '{z1}' and '{z2}'."
            )

        max_link_capacity = 1
        if 'max_link_capacity' in metadata:
            try:
                max_link_capacity = int(metadata['max_link_capacity'])
                if max_link_capacity <= 0:
                    raise ValueError()
            except ValueError:
                raise ParseError(
                    f"Line {line_number}: 'max_link_capacity' "
                    f"must be a positive integer."
                )

        self.data.connections.append(Connection(z1, z2, max_link_capacity))
        self._parsed_connections.add(edge_key1)

    def _validate_final_state(self) -> None:
        """Validate that the parsed map has all required elements.

        Raises:
            ParseError: If required elements are missing.
        """
        if not self._nb_drones_found:
            raise ParseError("Error: Missing 'nb_drones' definition.")
        if not self.data.start_hub:
            raise ParseError(
                "Error: Missing exactly one 'start_hub' definition."
                )
        if not self.data.end_hub:
            raise ParseError(
                "Error: Missing exactly one 'end_hub' definition."
                )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parse.py <map_file>")
        sys.exit(1)

    try:
        parser = Parser(sys.argv[1])
        map_data = parser.parse()
        print("Successfully parsed map:")
        print(f"  Drones: {map_data.nb_drones}")
        print(f"  Start: {map_data.start_hub}")
        print(f"  End: {map_data.end_hub}")
        print(f"  Zones: {len(map_data.zones)}")
        print(f"  Connections: {len(map_data.connections)}")
    except ParseError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
