
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with combat and magical capabilities."""

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 health: int,
                 damage: int,
                 defense: int,
                 gen_mana: int):
        """Initialize elite card with combat and magic stats."""
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, health, damage, defense)
        Magical.__init__(self, gen_mana)

    def play(self, game_state: dict) -> dict:
        """Play elite card and activate its abilities."""
        if self.is_playable(game_state['available_mana']) <= 0:
            return {
                'success': False,
                'message': f'Not enough mana to play {self.name}',
                'updated_state': game_state
            }

        game_state['available_mana'] -= self.cost
        if game_state['available_mana'] <= 0:
            game_state['available_mana'] = 0

        game_state['active_cards'] = game_state.get('active_cards', [])
        game_state['active_cards'].append(self.name)

        return {
            'success': True,
            'message': f'{self.name} has been played!',
            'game_state': game_state,
            'card_stats': self.get_card_info()
        }

    def attack(self, target: str) -> dict:
        """Attack target using melee combat."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            "combat_type": "melee"

        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage using defense stat."""
        damage_reciv = incoming_damage - self.defense
        damage_reciv = 0 if damage_reciv < 0 else damage_reciv

        blocked = incoming_damage - damage_reciv

        live = self.health - damage_reciv

        return {
            "defender": self.name,
            "damage_taken": damage_reciv,
            "damage_blocked": blocked,
            "still_alive": True if live > 0 else False
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics."""
        return {
            'name': self.name,
            'attack_power': self.damage,
            'defense': self.defense,
            'health': self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast spell on target list."""
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel mana and return total mana available."""
        total_mana = self.gen_mana + amount

        return {
            "channeled": self.gen_mana,
            "total_mana": total_mana
        }

    def get_magic_stats(self) -> dict:
        """Return magical statistics."""
        return {
            "name": self.name,
            "mana_generate": self.gen_mana,
            "ability": "Transfrom time in to mana"
        }
