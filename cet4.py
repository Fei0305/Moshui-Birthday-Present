import pymysql
import random


def cet4_word() -> None:
    """ 随机抽取CET4单词
    :return word: 单词,
            word_read: 发音,
            word_mean: 翻译,
            sample: 例句
    """
    # 连接数据库
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='peerless187',
        database='word'
    )

    cursor = db.cursor()
    # SQL查询语句
    sql = "SELECT * FROM cet4 WHERE id={}".format(random.randint(1, 4415))
    # sql = "SELECT * FROM cet4 WHERE id=5"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()[0]
        word = result[1]
        # word_read = '/' + result[2].split('\n')[1][3:-1] + '/'
        word_mean_list = result[3].split('\n')
        samples_list = result[6].split('\n')

        if len(word_mean_list) > 1:
            if len(word_mean_list[0].split('；')) > 1:
                word_mean = word_mean_list[0].split('；')[0] +\
                            ';' +\
                            word_mean_list[0].split('；')[1] +\
                            '  ' +\
                            word_mean_list[1].split('；')[0]
            else:
                word_mean = word_mean_list[0].split('；')[0] +\
                '  ' +\
                word_mean_list[1].split('；')[0]

        else:
            word_mean = word_mean_list[0]

        if len(word_mean) > 23:
            word_mean = word_mean[:23] + '...'

        if samples_list == ['']:
            sample = 'No example,Maybe you can ask your baby Fei :)'
        else :
            sample = samples_list[0]


    except BaseException as e:
        print("ERROR:")
        print(repr(e))

    db.close()

    return word, word_mean, sample


if __name__ == '__main__':
    word, word_mean, sample = cet4_word()
    print(word)
    print(word_mean)
    print(sample)