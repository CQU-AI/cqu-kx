from cqu_kx.config.config import config, Config
from cqu_kx.utils import check_user, log
from cqu_kx.version import __version__


def main():
    pass


def console_main():
    import argparse

    def parse_args() -> argparse.Namespace:
        """Parse the command line arguments for the `cqu jwc` binary.

        :return: Namespace with parsed arguments.
        """
        parser = argparse.ArgumentParser(
            prog="jwc",
            description="第三方 重庆大学 成绩查询",
        )

        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"CQU_jwc {__version__}",
            help="显示版本号",
        )
        parser.add_argument(
            "-c",
            "--config_path",
            help="查询配置文件路径",
            action="store_true",
        )
        parser.add_argument(
            "-r",
            "--reset",
            help="重置配置项",
            action="store_true",
        )
        parser.add_argument(
            "-u",
            "--username",
            help="学号",
            type=int,
            default=config["user_info"]["username"],
        )
        parser.add_argument(
            "-p",
            "--password",
            help="密码",
            type=str,
            default=config["user_info"]["password"],
        )
        parser.add_argument(
            "-o",
            "--output",
            help="成绩输出路径",
            type=str,
            default=config["output"]["path"],
        )

        return parser.parse_args()

    args = parse_args()
    if args.reset:
        Config.reset()
        log("已重置配置文件")
    if args.config_path:
        log(f"配置文件位于{Config.path}\n")
        sys.exit()

    config.dump()

    main()


if __name__ == "__main__":
    main()