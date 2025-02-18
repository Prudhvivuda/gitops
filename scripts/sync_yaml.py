import yaml
import os

def sync_yaml_files():
    # Load config from folder B
    config_path = 'B/config.yaml'
    if not os.path.exists(config_path):
        print("Error: config.yaml not found in B/")
        return

    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Ensure output directory exists
    output_dir = 'B/merged_yaml'
    os.makedirs(output_dir, exist_ok=True)

    # Process each YAML file in folder A
    for filename in os.listdir('A'):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            file_path = f'A/{filename}'
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)

            # Replace values using config.yaml in B
            env = data.get('environment', 'dev')
            if env in config:
                merged_data = merge_yaml(data, config[env])
            else:
                print(f"Warning: No config found for environment '{env}' in {filename}. Skipping update.")
                merged_data = data  # Keep original content

            # Save merged YAML as a new file
            output_file_path = f'{output_dir}/{filename}'
            with open(output_file_path, 'w') as output_file:
                yaml.dump(merged_data, output_file, default_flow_style=False)

            print(f"Merged YAML saved: {output_file_path}")

    print("YAML sync process completed!")

def merge_yaml(original, updates):
    """
    Recursively merges `updates` into `original` without overwriting entire dictionaries.
    """
    if isinstance(original, dict) and isinstance(updates, dict):
        for key, value in updates.items():
            if key in original and isinstance(original[key], dict):
                original[key] = merge_yaml(original[key], value)
            else:
                original[key] = value
    return original

if __name__ == "__main__":
    sync_yaml_files()
