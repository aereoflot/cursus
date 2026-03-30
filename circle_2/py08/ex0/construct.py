import sys
import os
import site


def matrix_status():

    try:
        act_eject = sys.prefix
        py_location = sys.base_prefix
        lib_instaled = site.getsitepackages()
        virtual_env = os.path.basename(sys.prefix)

        if act_eject == py_location:
            print("\nMATRIX STATUS: You're still plugged in")

            print(f"\nCurrent Python: {sys.executable}")
            print("Virtual Environment: None detected")

            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")

            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")
            print("\nThen run this program again.")

        else:
            print("\nMATRIX STATUS: Welcome to the construct")

            print(f"\nCurrent Python: {sys.executable}")
            print(f"Virtual Environment {virtual_env}")
            print(f"Environment Path: {act_eject}")

            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting "
                  "the global system")

            print(f"\nPackage installation path:\n{lib_instaled[0]}")

    except (AttributeError, TypeError):
        print("Something was wrong, check all before try again")


if __name__ == "__main__":
    matrix_status()
