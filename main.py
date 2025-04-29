import os
import subprocess
import traceback


def get_oriented_inps(inp_file):
    start_marker = "$              Site and Building Data"
    end_marker = "$              Materials / Layers / Constructions"

    with open(inp_file, 'r') as file:
        data_lines = file.readlines()

    # Locate section to search
    start_index = next((i for i, line in enumerate(data_lines) if start_marker in line), None)
    end_index = next((i for i, line in enumerate(data_lines) if end_marker in line), None)

    if start_index is None or end_index is None:
        print(f"Markers not found in {inp_file}. Skipping...")
        return

    section_lines = data_lines[start_index:end_index]
    azimuth_line_index = None
    current_azimuth = None

    # Check for existing AZIMUTH
    for i, line in enumerate(section_lines):
        if "AZIMUTH" in line:
            azimuth_line_index = start_index + i
            try:
                current_azimuth = int(line.split("=")[-1].strip())
            except ValueError:
                print("Invalid AZIMUTH value. Skipping...")
                return
            break

    # If not found, insert AZIMUTH = 0
    if azimuth_line_index is None:
        for i in range(start_index, end_index):
            if '"Building Data"' in data_lines[i] and 'HOLIDAYS' in data_lines[i + 1]:
                azimuth_line_index = i + 1
                current_azimuth = 0
                data_lines.insert(azimuth_line_index, f'   AZIMUTH          = {current_azimuth}\n')
                break

    # Create 3 new files by rotating +90° each
    base_dir = os.path.dirname(inp_file)
    base_name = os.path.basename(inp_file)
    name_no_ext, ext = os.path.splitext(base_name)

    for i in range(1, 4):
        new_azimuth = (current_azimuth + i * 90) % 360
        new_lines = data_lines.copy()
        new_lines[azimuth_line_index] = f'   AZIMUTH          = {new_azimuth}\n'
        new_file = os.path.join(base_dir, f"{new_azimuth}_{name_no_ext}{ext}")
        with open(new_file, 'w') as f:
            f.writelines(new_lines)
        print(f"Generated: {new_file}")


# --- Main Runner ---
if __name__ == "__main__":
    inp_path = input("Enter full path to your .inp file: ").strip('"')
    if not os.path.isfile(inp_path):
        print("Invalid file path. Please check and try again.")
    else:
        get_oriented_inps(inp_path)

bat_file_path = r"D:\EDS\S2302_eQuest_Automation\S2302.6_MEPCalculator\script.bat"
subprocess.call([bat_file_path], shell=True)

next_script = r"D:\EDS\S2302_eQuest_Automation\S2302.6_MEPCalculator\file.py"
try:
    print(f"\nExecuting Streamlit App: {next_script}")
    result = subprocess.run(['streamlit', 'run', next_script], check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Streamlit app {next_script} failed with exit code {e.returncode}")
    print("Error Output:\n", e.stderr)
except Exception as e:
    print(f"Failed to run script {next_script}: {e}")
    traceback.print_exc()
finally:
    print("Moving to next step...")