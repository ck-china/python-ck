#导入到mongodb
import pymongo,pymysql,redis,json
def save_to_mongodb():
    #创建一个redis数据库链接
    redisCli=redis.StrictRedis(host='localhost',port=6379)
    #创建一个mongodb连接
    mongoCli=pymongo.MongoClient(host='localhost',port=27017)
    #获取mongodb的数据库
    db=mongoCli['qidian']
    collection=db['QD']

    #从redis数据库里取出数据
    while True:
        source,data=redisCli.blpop('mycrawler_edis:items',timeout=1)
        #这里取出来的data是个二进制数据的字符串，需要解码，然后用json.loads转为python类型数据
        str_data=data.decode('utf8')
        data=json.loads(str_data)
        #将数据存到mongodb
        collection.insert(data)

if __name__ == "__main__":
    save_to_mongodb()