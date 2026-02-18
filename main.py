import webbrowser
import time

import pyautogui
import yaml

from typing import Any, Optional
from dataclasses import dataclass

@dataclass
class ScreenConfig:
    infoskjerm_id: str
    nettsider: Optional[list[str]] = None
    vis_standardnettsider: Optional[bool] = None
    fanetid: Optional[int] = None
    browser: Optional[str] = None


    @classmethod
    def from_dict(cls, screen_id: str, config: dict[str, Any]) -> "ScreenConfig":
        return cls(infoskjerm_id=screen_id,
                   fanetid=config.get("fanetid"),
                   vis_standardnettsider=config.get("vis_standardnettsider"),
                   nettsider=config.get("nettsider"),
                   browser=config.get("browser"))

def load_screen_id_from_file(filename: str = "INFOSKJERM_ID")  -> str:
    try:
        with open(filename) as file:
            screen_id = file.read().strip()
    except FileNotFoundError:
        screen_id = "standard"

    return screen_id


def load_config(filename: str = "nettsider.yaml") -> dict[str,ScreenConfig]:
    with open(filename) as file:
        yaml_config = yaml.safe_load(file)

    raw_screen_configs= yaml_config["infoskjermer"]

    screen_configs = {key:ScreenConfig.from_dict(screen_id=key, config=value) for key, value in raw_screen_configs.items()}


    return screen_configs


def get_config(screen_configs: dict[str, ScreenConfig], screen_id: str) -> ScreenConfig:
    if screen_id in screen_configs.keys():
        return screen_configs[screen_id]
    else:
        return screen_configs["standard"]


def prepare_config(config: ScreenConfig, standard_config: ScreenConfig) -> ScreenConfig:
    if not config.fanetid:
        config.fanetid = standard_config.fanetid

    if not config.nettsider:
        config.nettsider = []

    if not config.browser:
        config.browser = standard_config.browser

    if not config.fanetid:
        config.fanetid = standard_config.fanetid

    if config.vis_standardnettsider:
        config.nettsider.extend(standard_config.nettsider)

    return config


def open_tabs(config: ScreenConfig) -> None:
    for nettside in config.nettsider:
        webbrowser.open(nettside)
        time.sleep(30)


def fullscreen(config: ScreenConfig) -> None:
    if config.infoskjerm_id == "lokalmac":
        command = ("ctrl","command", "f")
    else:
        command = "f11"

    pyautogui.hotkey(*command)

def switch_between_tabs(config:ScreenConfig) -> None:
    command = ("ctrl", "tab")
    while True:
        pyautogui.hotkey(*command)
        time.sleep(config.fanetid)


def main():
    screen_id = load_screen_id_from_file()
    screen_configs=load_config()

    standard_config = get_config(screen_configs=screen_configs, screen_id="standard")
    config = get_config(screen_configs=screen_configs, screen_id=screen_id)

    prepared_config = prepare_config(config=config, standard_config=standard_config)

    open_tabs(config=prepared_config)
    fullscreen(config=prepared_config)
    switch_between_tabs(config=prepared_config)


if __name__ == "__main__":
    main()
