from logfile import logclass


class logtest:
    def loggerT(self):
        logdata = logclass.logger()
        logdata.info("测试TestUserTasks")


if __name__ == '__main__':
    logtest().loggerT()
