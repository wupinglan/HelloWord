import logging
import time

def initLogging(self,message):
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    logging.basicConfig(
        level    = logging.DEBUG,
        format   = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
        # datefmt  = '%a, %d %b %Y %H:%M:%S',
        filename = "/Users/wupinglan/Desktop/feautures/features/logs/" + filename + ".log",                    
        filemode = 'w+')

    #添加StreamHandler在控制台也打印出来
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # console.propagate = 1
    formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(message)

