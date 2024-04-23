import paramiko

from apps.utils import Logger
logger1 = Logger().logger


def auto_linux_cmd(servers: list, commands: list, local_filepath: str = "", remote_filepath: str = "/usr/local/src/"):
    for s_info in servers:
        try:
            # 创建SSH客户端对象
            client = paramiko.SSHClient()
            # 设置自动添加主机密钥
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接到目标服务器
            client.connect(hostname=s_info["host"], port=s_info["port"], username=s_info["username"],
                           password=s_info["password"])
            name = s_info["name"]
            logger1.info("connected !!! current server name:  %s", name)
            if local_filepath != "":
                sftp = client.open_sftp()
                logger1.info("local_filepath: %s remote_filepath: %s \n" % (local_filepath, remote_filepath))
                sftp.put(local_filepath, remote_filepath)
                logger1.info("upload success !!!")
            cmds = ""
            for cmd_1 in commands:
                cmds += cmd_1
                cmds += ';'
            logger1.info("cmd: %s" % cmds)
            stdin, stdout, stderr = client.exec_command(cmds)
            # 输出命令结果
            logger1.info('Command output:\n')
            logger1.info(stdout.read().decode())
            logger1.info('Command err output:\n')
            logger1.info(stderr.read().decode())

        except Exception as e:
            logger1.error("Error connecting to server or executing the command. name: %s", s_info["name"])
            logger1.error(e)
            return
        finally:
            client.close()
    logger1.info("All execution completed")
