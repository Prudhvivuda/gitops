import os
import yaml

A_FOLDER = "A"
B_FOLDER = "B"
CONFIG_PATH = "config/config.yaml"

def load_yaml(file_path):
    """Loads a YAML file and returns its contents as a dictionary."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    """Saves a dictionary as a YAML file."""
    with open(file_path, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

def update_files():
    """Reads config.yaml, updates A folder files, and saves to B folder."""
    config = load_yaml(CONFIG_PATH)
    os.makedirs(B_FOLDER, exist_ok=True)

    for file_info in config.get("file", []):
        file_name = file_info["name"].strip()
        file_path_a = os.path.join(A_FOLDER, file_name)
        file_path_b = os.path.join(B_FOLDER, file_name)

        if os.path.exists(file_path_a):
            data = load_yaml(file_path_a)
            for key, value in file_info.get("keys", {}).items():
                if key in data:
                    data[key] = value  # Override values based on config.yaml
            save_yaml(data, file_path_b)

if __name__ == "__main__":
    update_files()
