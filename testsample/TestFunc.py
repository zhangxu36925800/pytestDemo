#jsonpath
import json
import jsonpath

teststr = '{"total":1,"rows":[{"createTime":"2022-01-07 11:16:47","id":41,"operater":"\xe6\x98\x9f\xe7\xa9\xba\xe6\xa2\xa6\xe8\xaf\xad","projectCode":"01234567","projectName":"test1","status":"0"}]}'
json_str = json.loads(teststr) #反序列化为dic对象
aa = json_str["total"]
# str_json = json.dumps(json_str)#序列化为json字符串
# projectCode = jsonpath.jsonpath(json_str,'rows[?(@.projectCode)]')#获取json中rows数组中包含projectCode的所有值
projectCode = jsonpath.jsonpath(json_str,'$..projectCode') #jsonpath解析获取json中book下的所有projectCode值


# print(json_str)
print(projectCode)
