import sys

from cqu_jxgl import Student, jxgl_config

from cqu_kx.config.config import config, Config
from cqu_kx.core import get_course, get_quota
from cqu_kx.utils import log, check_output_path
from cqu_kx.version import __version__


def write_table(table):
    with open(config["output"]["path"], "w") as f:
        print("课程名称,授课教师,可选人数", file=f)
        for row in table:
            print(",".join(row), file=f)
    log(f'查询结果已经保存到{config["output"]["path"]}')


def main():
    check_output_path()
    student = Student()

    course = get_course(student)
    quota_table = get_quota(student, course)

    if config['behavior']['output']:
        write_table(quota_table)


def console_main():
    import argparse

    def parse_args() -> argparse.Namespace:
        """Parse the command line arguments for the `cqu-kx` binary.

        :return: Namespace with parsed arguments.
        """
        parser = argparse.ArgumentParser(prog="cqu-kx", description="第三方重庆大学课程可选人数查询工具－“快选!!”", )

        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"cqu-kx {__version__}",
            help="显示版本号",
        )
        parser.add_argument(
            "-c", "--config_path", help="查询配置文件路径", action="store_true",
        )
        parser.add_argument(
            "-r", "--reset", help="重置配置项", action="store_true",
        )
        parser.add_argument(
            "-u",
            "--username",
            help="学号",
            type=int,
            default=None,
        )
        parser.add_argument(
            "-p",
            "--password",
            help="密码",
            type=str,
            default=None,
        )
        parser.add_argument(
            "-n",
            "--no-output",
            help="不输出结果文件",
            action="store_true",
        )
        parser.add_argument(
            "-o", "--output", help="结果输出路径", type=str, default=config["output"]["path"],
        )

        return parser.parse_args()

    args = parse_args()
    if args.reset:
        Config.reset()
        log("已重置配置文件")
    if args.config_path:
        log(f"配置文件位于{Config.path}\n")
        sys.exit()
    if args.no_output:
        config['behavior']['output'] = False
    if args.username is not None:
        jxgl_config['user_info']['username'] = args.username
    if args.password is not None:
        jxgl_config['user_info']['password'] = args.password

    config.dump()

    main()


if __name__ == "__main__":
    main()
