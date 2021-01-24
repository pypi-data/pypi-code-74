"""Generate MQTT file."""
from collections import defaultdict
import json
from typing import Dict

from .model import Config, Integration

BASE = """
\"\"\"Automatically generated by hassfest.

To update, run python3 -m script.hassfest
\"\"\"

# fmt: off

MQTT = {}
""".strip()


def generate_and_validate(integrations: Dict[str, Integration]):
    """Validate and generate MQTT data."""

    data = defaultdict(list)

    for domain in sorted(integrations):
        integration = integrations[domain]

        if not integration.manifest:
            continue

        mqtt = integration.manifest.get("mqtt")

        if not mqtt:
            continue

        for topic in mqtt:
            data[domain].append(topic)

    return BASE.format(json.dumps(data, indent=4))


def validate(integrations: Dict[str, Integration], config: Config):
    """Validate MQTT file."""
    mqtt_path = config.root / "homeassistant/generated/mqtt.py"
    config.cache["mqtt"] = content = generate_and_validate(integrations)

    if config.specific_integrations:
        return

    with open(str(mqtt_path)) as fp:
        if fp.read().strip() != content:
            config.add_error(
                "mqtt",
                "File mqtt.py is not up to date. Run python3 -m script.hassfest",
                fixable=True,
            )
        return


def generate(integrations: Dict[str, Integration], config: Config):
    """Generate MQTT file."""
    mqtt_path = config.root / "homeassistant/generated/mqtt.py"
    with open(str(mqtt_path), "w") as fp:
        fp.write(f"{config.cache['mqtt']}\n")
