import os
from os import path
import jieba
import re
import jieba.analyse
import wordcloud
import matplotlib.pyplot as plt


def create_cloud(sightitem):
    washed = re.sub('[^\u4e00-\u9fa5]+', ' ', sightitem['comment'])

    freq_dict = {}
    tags = jieba.analyse.extract_tags(washed, topK=40, withWeight=True)
    for tag in tags:
        freq_dict[tag[0]] = tag[1]

    wc = wordcloud.WordCloud(
        width=1000,
        height=700,
        font_path="./assets/SourceHanSansCN-Normal.ttf",
        background_color=None,
        colormap=plt.get_cmap('YlGnBu'))
    wc.generate_from_frequencies(freq_dict)
    filename = sightitem['id'] + '.png'
    cloud_path = path.join(os.getcwd(), 'clouds', filename)
    wc.to_file(cloud_path)
    sightitem['wordcloud_path'] = cloud_path
