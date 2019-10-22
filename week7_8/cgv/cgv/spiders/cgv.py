# -*- coding: utf-8 -*-
import scrapy
import json

class cgv(scrapy.Spider):
    name = "cgv"
    url = 'http://ticket.cgv.co.kr/CGV2011/RIA/CJ000.aspx/CJ_HP_SCHEDULE_TOTAL_DEFAULT'
    def start_requests(self):

        return [
                scrapy.http.JSONRequest('http://ticket.cgv.co.kr/CGV2011/RIA/CJ000.aspx/CJ_HP_SCHEDULE_TOTAL_MOVIE',
                   data={
                       'ISNormal': "ECFppiyFz/nvSGsg7VwPQw==",
                       'Language': "zqWM417GS6dxQ7CIf65+iA==",
                       'PlayYMD': "nG6tVgEQPGU2GvOIdnwTjg==",
                       'REQSITE': "x02PG4EcdFrHKluSEQQh4A==",
                       'ScreenRatingCd': "kXwoR3tnLM/+Tu0BILP3Qg==",
                       'TheaterCd': "LMP+XuzWskJLFG41YQ7HGA=="
                    }),
                scrapy.http.JSONRequest('http://ticket.cgv.co.kr/CGV2011/RIA/CJ000.aspx/CJ_HP_SCHEDULE_TOTAL_PLAY_YMD',
                    data={
                        'ISNormal': "ECFppiyFz/nvSGsg7VwPQw==",
                        'Language': "zqWM417GS6dxQ7CIf65+iA==",
                        'MovieGroupCd': "nG6tVgEQPGU2GvOIdnwTjg==",
                        'MovieTypeCd': "nG6tVgEQPGU2GvOIdnwTjg==",
                        'REQSITE': "x02PG4EcdFrHKluSEQQh4A==",
                        'SOUNDX_YN': "nG6tVgEQPGU2GvOIdnwTjg==",
                        'ScreenRatingCd': "kXwoR3tnLM/+Tu0BILP3Qg==",
                        'Subtitle_CD': "nG6tVgEQPGU2GvOIdnwTjg==",
                        'TheaterCd': "LMP+XuzWskJLFG41YQ7HGA==",
                        'Third_Attr_CD': "nG6tVgEQPGU2GvOIdnwTjg=="
                    })
                ]

    def parse(self, response):
        print("==========")
        print(response)
        jsonresponse = json.loads(response.body_as_unicode())
        # print(jsonresponse['d']['data']['DATA'])
        # print(jsonresponse)

