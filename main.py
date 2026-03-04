import datetime
import webbrowser
import time

import pyautogui
import yaml


from typing import Any, Optional
from dataclasses import dataclass, field

from logger import Logger

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


@dataclass
class TimeToRefresh:
    ttr: datetime.timedelta
    last_refresh_datetime: datetime.datetime = field(init=False)


    def __post_init__(self):
        self.last_refresh_datetime = datetime.datetime.now()

    def should_refresh(self) -> bool:
        if  datetime.datetime.now() >  self.last_refresh_datetime +  self.ttr:
            self.last_refresh_datetime = datetime.datetime.now()
            return True
        else:
            return False




def load_screen_id_from_file(filename: str = "INFOSKJERM_ID")  -> str:
    try:
        with open(filename) as file:
            screen_id = file.read().strip()
    except FileNotFoundError:
        screen_id = "standard"

    return screen_id


def load_config(filename: str = "nettsider.yaml") -> dict[str,ScreenConfig]:
    try:
        with open(filename) as file:
            yaml_config = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Config for screens was not found! Default name is nettsider.yaml.")

    try:
        raw_screen_configs= yaml_config["infoskjermer"]
    except KeyError:
        raise KeyError("The field 'infoskjermer' was not found in config file.")

    screen_configs = {key:ScreenConfig.from_dict(screen_id=key, config=value)
                      for key, value in raw_screen_configs.items()}

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
        time.sleep(config.fanetid)


def fullscreen(config: ScreenConfig) -> None:
    if config.infoskjerm_id == "lokalmac" or "utsikt-test":
        command = ["ctrl","command", "f"]
    else:
        command = ["f11"]

    pyautogui.hotkey(*command)

def scroll_n_times(config: ScreenConfig, n: int, down: bool) -> None:
    scroll_down_command = ["pagedown"]
    scroll_up_command = ["pageup"]

    for i in range(n):
        if down:
            pyautogui.hotkey(*scroll_down_command)
        elif not down:
            pyautogui.hotkey(*scroll_up_command)
        else:
            raise ValueError(f"down input must be a bool, but got {type(down)}!")

    time.sleep(config.fanetid)


def switch_between_tabs(config:ScreenConfig, logger: Logger,  n_scroll: int = 1) -> None:
    switch_tab_command = ["ctrl", "tab"]
    refresh_command =["ctrl", "r"]

    time_to_refresh = TimeToRefresh(ttr=datetime.timedelta(minutes=1))

    count = 0
    while True:
        if time_to_refresh.should_refresh():
            for _ in range(len(config.nettsider)):
                count += 1
                pyautogui.hotkey(*refresh_command)
                time.sleep(config.fanetid)
                pyautogui.hotkey(*switch_tab_command)
                time.sleep(config.fanetid)


        pyautogui.hotkey(*switch_tab_command)
        count += 1
        time.sleep(config.fanetid)

        scroll_n_times(config=config, n=n_scroll, down=False)
        scroll_n_times(config=config, n=n_scroll, down=True)


        if count % 10*len(config.nettsider) == 0:
            logger.info(f"Karusellen har rullet {int(count/len(config.nettsider))}")


def main():
    logger = Logger(name="Infoskjerm karusell")
    logger.info("Starter karusell...")
    screen_id = load_screen_id_from_file()

    logger.info(f"Bruker {screen_id} config for karusellen.")
    screen_configs=load_config()

    standard_config = get_config(screen_configs=screen_configs, screen_id="standard")
    config = get_config(screen_configs=screen_configs, screen_id=screen_id)

    prepared_config = prepare_config(config=config, standard_config=standard_config)

    logger.info(f"Åpner faner...")
    open_tabs(config=prepared_config)
    fullscreen(config=prepared_config)
    switch_between_tabs(config=prepared_config, logger=logger)


if __name__ == "__main__":
    main()
