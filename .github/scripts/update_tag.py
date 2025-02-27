import os
import re
import yaml

# Path to the config.yaml file
config_path = '.github/config/config.yaml'

# Function to update the tag in config.yaml
def update_tag():
    # Get the current version from the GitHub tag (using the environment variable GITHUB_REF)
    tag_ref = os.environ.get('GITHUB_REF')
    
    if not tag_ref or not tag_ref.startswith('refs/tags/v'):
        raise ValueError("Tag not found or not a valid version tag.")

    # Extract the version number from the tag reference (e.g., 'v1.2.3')
    current_version = tag_ref.replace('refs/tags/', '')

    # Increment the patch version
    major, minor, patch = map(int, current_version.lstrip('v').split('.'))
    new_patch = patch + 1
    new_version = f"{major}.{minor}.{new_patch}"

    # Read the current config.yaml file
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Update the tag version in config.yaml
    if 'tag' in config:
        config['tag'] = f'v{new_version}'
    else:
        config['tag'] = f'v{new_version}'

    # Write the updated config.yaml back
    with open(config_path, 'w') as file:
        yaml.safe_dump(config, file)

    print(f"Updated tag version to {new_version}")

if __name__ == "__main__":
    update_tag()
