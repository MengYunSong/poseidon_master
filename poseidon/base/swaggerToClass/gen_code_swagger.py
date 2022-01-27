# -*- coding:utf8 -*-
import requests, os,sys, codecs
import json, random

from .CodeGeneratorBackend import CodeGeneratorBackend
from .CodeMode import api_obj_code_model, test_case_code_model


class CodeModel(object):
    def __init__(self):
        self.para = "({value},{expect_status_code},\"{test_case_desc}\"),\n"
        # self.para = "[\"{test_case_desc}\",{expect_status_code},{value}],\n"


class Print(object):

    def __init__(self, url='http://qacbz-costpersales.soa.yeshj.com/rest/swagger.json', base_name='nc'):
        self.c = CodeGeneratorBackend()
        self.c.begin(tab="    ")
        self.base_name = base_name
        self.url = url
        self.swagger_apis = self.get_api_info()  # 从swagger接口获取接口信息
        self.host = self.swagger_apis['host']  # 获取host
        # self.host = self.swagger_apis['info']['title']  # 获取host
        self.definitions = self.Definitions(definitions=self.swagger_apis.get("definitions"),
                                            print_instance=self)
        # self.deal_swagger_result()  # 从swagger返回结果中获取其他接口的信息

    def print_test_case(self, file_path=None):
        """
        master function 用于打印基本用例
        file_path: file_path 不传默认当前路径
        :return:
        """

        # 开始遍历每个接口
        apis_dict = self.swagger_apis.get('paths')
        for uri, api in apis_dict.items():
            # 进入单个接口,打印用例import和setup等方法
            # self.c.write("\n\n")
            # self.c.write("# 开始打印接口{uri}的用例====================================\n".format(uri=uri))
            # self.print_test_case_header(class_name=)
            for method, other_api in api.items():
                api_obj = self.RestfulApi(uri=uri, method=method, api_info=other_api, print_instance=self, base_name=self.base_name)
                api_obj.generate_test_case_header()
                api_obj.analyze_the_api_test_case()
                self.write_file(self.c.end(), file_path, '{0}.py'.format(api_obj.case_file_name))
                self.c.code = []

    def write_file(self, data, file_path=None, file_name='test.txt'):
        if isinstance(data, dict):
            data = json.dumps(data)

        if file_path:
            file_path = file_path
        else:
            if sys.platform == "win32" or sys.platform == "win64":
                file_path = os.getcwd() + '\\'
            else:
                file_path = os.getcwd() + '/'
        with codecs.open(file_path + file_name, 'a+', encoding='utf-8') as f:
            f.write(data)

    def analyze_test_data(self, file_path=None):
        """
        master function 打印测试数据所有内容
        file_path: file_path 不传默认当前路径
        :return:
        """

        # 打印import部分
        self.c.write(api_obj_code_model.generate_import(file_name=self.base_name))

        # 打印每个接口的test data
        apis_dict = self.swagger_apis.get('paths')
        for uri, api in apis_dict.items():
            print(uri)
            for method, other_api in api.items():
                api_obj = self.RestfulApi(host=self.host, uri=uri, method=method, api_info=other_api, print_instance=self, base_name=self.base_name)
                api_obj.analyze_api_test_data()

        self.write_file(self.c.end(), file_path=file_path, file_name=self.base_name + ".py")
        # print(self.c.end())

    def get_api_info(self):
        """
        请求swagger信息并处理
        :return:
        """
        return json.loads(self.send_request(self.url))  # 返回的是json格式

    def analyze_definitions(self, define):
        if define:
            self.definitions.analyze_define(define)

    def get_definitions_params_dict(self,define):
        """
        该方法会返回定义模块中的每个参数的详细属性列表
        :param define:
        :return:
        """
        return self.definitions.get_definitions_params_dict(define)


    def send_request(self,url):
        cookies = {
                   'dbtoolsauth': '0001ec35de.91c85bbe830548dabaeef219ce17f3f2',
                   'ClubAuth': '99A1D24D277CFA2B078BD62182B651B64A52098F59984A42C4F353FDE19565B4456B3B97BBEABDDCAB9E5B2001A4F797DE81F10698ABE06ED4C33CABA4D5D49A544AD53CB8B70BFB90D04B8FA22DF86EB07341866E802C413C60C535ECCABD0E39B236369720548BB4A4F13FE800B9F6AF4337E42E5BFB5F30C56C270EC01336A4224A97B3E9E5C55A6E140A88332F97C00F2657CF18460AD6980AABDF6BF2D7AB93EF68',
                   'hj_token': 's_1e339d1eb04dd1e8dddf53e1483a7cb5|M2QxOGQ0Yg==',
                   'JSESSIONID': "275321836D6DDF891903E9F9035EBA8E",
                   }
        headers = dict(Cookie="seraph.confluence=38241931%3A1f8e23558cd13dab1182243fdf0ee77859b5a375; dbtoolsauth=0001ec35de.91c85bbe830548dabaeef219ce17f3f2; ClubAuth=99A1D24D277CFA2B078BD62182B651B64A52098F59984A42C4F353FDE19565B4456B3B97BBEABDDCAB9E5B2001A4F797DE81F10698ABE06ED4C33CABA4D5D49A544AD53CB8B70BFB90D04B8FA22DF86EB07341866E802C413C60C535ECCABD0E39B236369720548BB4A4F13FE800B9F6AF4337E42E5BFB5F30C56C270EC01336A4224A97B3E9E5C55A6E140A88332F97C00F2657CF18460AD6980AABDF6BF2D7AB93EF68; hj_token=s_1e339d1eb04dd1e8dddf53e1483a7cb5|M2QxOGQ0Yg==; ClubAuth_DEV=98D63412C3F380F5050BB62057A4721D2AEFFAE64BF8625564F6EB4D16B283C3DEFD9F9E483D5DC817083286572756351693823916414A5A03FC3E50EEB6BC181A05772986830422AABBBAEF0D5C9BEC3573B97E2C0D0B2DF834A34CBCB45B4CD54EF9820110752D8B67516C4F814F55874DADB43FFF7E6F7FB25550B69408D870A9E91064D579163CA7C899369BBA1E1C1BFB1FF20FF98E7787A884; JSESSIONID=275321836D6DDF891903E9F9035EBA8E; crowd.token_key=OdZ8Yux0sdOX3ld8HqjJDw00; mywork.tab.tasks=False")
        #result = requests.get(url=url, cookies=cookies, headers=headers)
        result = requests.get(url=url, cookies=None, headers=None)
        # print result.text
        return result.text




    class RestfulApi(object):
        def __init__(self, host=None, uri=None, method=None, api_info=None, base_name=None, print_instance=None):
            self.print_instance = print_instance
            self.c = print_instance.c  # 将print类中的打印对象传入
            self.host = host
            self.uri = uri
            self.api = api_info
            self.class_name = self.get_class_name() if self.uri else None   # 生成对象模型名称
            self.case_file_name = self.get_case_file_name() if self.uri else None   # 生成测试用例类名称
            self.base_name = base_name
            # api_some_info = self.get_api_some_info()
            self.api_desc = api_info.get("summary") if api_info else None
            self.method = method
            self.model = CodeModel()

        def get_class_name(self):
            name = ''
            for s in self.uri.split('/'):
                if s == '':
                    continue
                if "?" in s:
                    s = s.split("?")[0]
                if s[0] == "{":
                    s = s[1:-1]
                if s[0] == "(" or s[0] == '（':
                    s = ''
                elif s[-1] == ')':
                    s = s[:-1]
                if "_" in s:
                    camel = []
                    for p in s.split("_"):
                        camel_p = p.capitalize()
                        camel.append(camel_p)
                    s = "".join(camel)
                name = name + s[0].upper() + s[1:]
            return name

        def get_case_file_name(self):
            name = 'test'
            for s in self.uri.split('/'):
                if s == '':
                    continue
                if "?" in s:
                    s = s.split("?")[0]
                name = name + '_' + s
            return name

        def generate_test_case_header(self):

            # 打印import部分
            self.c.write(test_case_code_model.generate_import(uri=self.uri, method=self.method, desc=self.api_desc, file_name=self.case_file_name))

            # 打印setup模块
            self.c.write(test_case_code_model.code_model_header(uri=self.uri,
                                                                api_class_name='Test' + self.class_name))
            self.c.write("\n")


        def print_pass(self):
            """
            方法中只有pass的时候可以用此方法
            :return:
            """
            self.c.indent()
            self.c.write("pass\n")
            self.c.dedent()

        def analyze_the_api_only_param_test_case(self, param_dict):
            """
            打印一个接口的某个参数的基本用例
            :param param_dict: 某个接口下一个参数的详细属性,需要传入
            :return:
            """

            param_name = param_dict.get('name').lower()

            self.c.indent()
            self.c.write("@pytest.mark.run([Env.qa], [Frequency.five_min])\n")
            self.c.write("@pytest.mark.parametrize('{param_name}', [\n".format(param_name=param_name))
            self.analyze_paramterized_body(is_required=param_dict.get('required'),
                                           type=param_dict.get('type'),
                                           format=param_dict.get('format'),
                                           desc=param_dict.get('description'),
                                           name=param_name
                                           )
            self.c.write("])\n")
            self.c.write("def test_{param_name}_base_case_{number}(self, {param_name}):\n".format(param_name=param_name,
                                                                                                                    number=random.randint(1, 99)))
            self.c.indent()
            desc = "{param_name}{desc}基本测试用例(自动化脚本生成)".format(param_name=param_name,
                                                                        desc=param_dict.get('description'))
            self.c.write("'''{desc}'''\n\n".format(desc=desc))
            self.c.write("api_obj = {api_class_name}\n".format(api_class_name= self.class_name + "()"))
            # todo 此处如果是嵌套或者list中的值不能这样写,之后处理
            self.c.write("# 嵌套的参数请自行赋值\n")
            self.c.write("api_obj.body.{param_name} = {param_name}[0]\n".format(param_name=param_name))
            # -----
            self.c.write("api_obj.send_request_then_check(status_exp={param_name}[1])\n".format(param_name=param_name))
            # self.c.write("api_obj.check()\n")
            self.c.dedent()
            self.c.dedent()
            self.c.write("\n")

        def analyze_paramterized_body(self, is_required=False, format=None, type=None, desc=None, name=None):
            value_normals = self.get_param_test_value(format=format, type=type).get('value_normals')  # 该参数的正常值
            value_errors = self.get_param_test_value(format=format, type=type).get('value_errors')   # 该参数的不符合类型的值
            self.c.indent()
            #  todo  根据属性给出基本用例的值
            # 添加参数为None情况的用例
            expect_status_code = -1 if is_required else 0  # 如果该参数是必传则期望结果是异常的用-1代替,否则是0
            test_case_desc = name + "不能为None" if is_required else name + "可以为None"
            self.c.write(self.model.para.format(value=None,
                                      expect_status_code=expect_status_code,
                                      test_case_desc=test_case_desc,
                                      ))
            # 添加参数为0情况的用例
            expect_status_code = 0  # 为0先默认为正确
            test_case_desc = name + "为0的情况"
            self.c.write(self.model.para.format(value=0,
                                      expect_status_code=expect_status_code,
                                      test_case_desc=test_case_desc,
                                      ))
            # 添加参数为空的情况的用例
            expect_status_code = 0
            test_case_desc = name + "为空字符串的情况"
            self.c.write(self.model.para.format(value="\"\"",
                                      expect_status_code=expect_status_code,
                                      test_case_desc=test_case_desc,
                                      ))

            # 添加参数为符合type类型的随机数
            if value_normals:
                expect_status_code = 0
                test_case_desc = '传入符合规则的随机值'
                for value_normal in value_normals:
                    self.c.write(self.model.para.format(value=value_normal,
                                              expect_status_code=expect_status_code,
                                              test_case_desc=test_case_desc,
                                              ))
            # 添加参数为不符合type类型的随机值
            if value_errors:
                expect_status_code = -1
                for value_error in value_errors:
                    test_case_desc = '传入不符合规则的随机值'.format(value_error=value_error)
                    self.c.write(self.model.para.format(value=value_error,
                                              expect_status_code=expect_status_code,
                                              test_case_desc=test_case_desc,
                                              ))
            self.c.dedent()

        def get_param_test_value(self, format=None, type=None):
            value_normals = []
            value_errors = []
            if type == 'object':
                value_errors.extend([1,'1',[]])  # 如果是一个对象属性,则默认添加如左侧的异常情况测试
            if type == 'array':
                value_normals.extend([[1,"\"test\"",[]],[]])
                value_errors.extend([1,"\"test\"",{}])
            if type == 'integer' or type == 'number':
                value_normals.extend([1,2,3])
                value_errors.extend(["\"test\"",999999999999,1.99,1.0,-1])
            if type == 'string' and format == 'date-time':
                value_normals.extend(["cb.currentTime()",
                                      "cb.getNewDiffTimeForCurrent(\"days\", 1, \"plus\")",
                                      "cb.getNewDiffTimeForCurrent(\"minutes\", 30)"])
                value_errors.extend([20170809,'20170809',[]])
            if type == 'string' and format == None:
                value_normals.extend(["\"test\""])
                value_errors.extend([1,[],{}])
            if type == 'string' and format == 'byte':
                value_normals.extend(["\"test\""])
                value_errors.extend([1,[],{}])
            if type == 'boolean':
                value_normals.extend([False,True])
                value_errors.extend([1,"\"test\"",[]])
            if type == 'number':
                value_normals.extend([1.00,1.01,1.001,1.0001,1])
                value_errors.extend(["\"test\"",[]])
            return dict(value_errors=value_errors,
                        value_normals=value_normals
                        )

        def analyze_the_api_test_case(self):
            """打印单个接口的用例"""

            parameters = self.api.get('parameters')  # 返回的是一个接口的参数列表
            if parameters:
                for param_dict in parameters:
                    if 'schema' in param_dict:
                        define = param_dict.get('schema').get('$ref')
                        # 下面需要返回模块定义中的参数详细情况
                        get_definitions_params_info_list = self.print_instance.get_definitions_params_dict(define)
                        for param_dict in get_definitions_params_info_list:
                            self.analyze_the_api_only_param_test_case(param_dict)
                    else:
                        # 如果不是body类型的参数直接根据参数属性打印用例就ok  # todo 1111就在该类中打印
                        # self.print_instance.print_the_api_only_param_test_case(self.class_name,self.test_case_name, param_dict)
                        self.analyze_the_api_only_param_test_case(param_dict=param_dict)

        def analyze_api_test_data(self):

            self.c.write(api_obj_code_model.generate_api_class(class_name=self.class_name,
                                                               base_name='',
                                                               api_desc=self.api_desc,
                                                               host=self.host,
                                                               uri=self.uri,
                                                               method=self.method))
            # self.c.dedent()  # 单个接口类中init方法结束
            self.c.indent()
            self.c.write('\n')
            self.c.write("class Body(BaseObj):\n")
            self.c.indent()  # 单个接口类中Body()类开始
            self.analyze_api_body()  # 打印该接口中的body类
            self.c.dedent()  # 单个接口类中Body()类结束
            self.c.write('\n')
            # 此处需要判断是否有必要创建Resp类
            resp_content = self.api.get('responses').get('200')
            if resp_content:
                self.c.write("class Resp(BaseObj):\n")
                self.c.indent()  # 单个接口类中Resp()类开始

                self.analyze_api_resp()  # 打印该接口中的resp类
                self.c.dedent()  # 单个接口类中Resp()类结束
            self.c.write("\n")
            # self.c.write("def check(self, **kwargs):\n")
            self.c.write(api_obj_code_model.generate_send_check_method())
            self.c.dedent()  # 单个接口类结束

        def analyze_api_resp(self):
            """
            print 单个api中的resp类
            :return:
            """

            self.c.write("def __init__(self):\n")
            self.c.indent()  # 单个接口类中Body()类中init方法开始
            define = self.api.get('responses',{}).get('200',{}).get("schema",{}).get("$ref")  # 返回的是resp的define地址路径
            self.c.write("super().__init__()\n")
            if define:

                self.print_instance.analyze_definitions(define)
            else:
                self.c.write('pass\n')

            self.c.dedent()  # 单个接口类中Body()类中init方法结束


        def analyze_api_body(self):
            """
            print 单个api中的body类
            :return:
            """
            self.c.write("def __init__(self, **kwargs):\n")
            self.c.indent()  # 单个接口类中Body()类中init方法开始
            self.c.write("super().__init__()\n")
            parameters = self.api.get('parameters')  # 返回的是一个接口的参数列表
            if parameters:
                for param_dict in parameters:
                    if 'schema' in param_dict:
                        define = param_dict.get('schema').get('$ref')
                        self.print_instance.analyze_definitions(define)
                    else:
                        #  todo 此处的默认值可以根据类型随机生成
                        self.c.write("self.{param_name} = None\n".format(param_name=param_dict.get('name')))

                # 增加super内容
                # self.c.write("ObjUtil.__init__(self)\n")
                # self.c.write("CommonBaseObj.__init__(self, dict_attributes=kwargs)\n")

            self.c.dedent()  # 单个接口类中Body()类中init方法结束

        # def get_api_some_info(self):
        #     """
        #     获取api的描述中的内容
        #     :return:
        #     """
        #     for method, other in self.api.items():
        #         return dict(method=method,
        #                     api_desc=other.get('summary'),
        #                     )



    class Definitions(object):
        def __init__(self,definitions,print_instance):
            self.definitions = definitions  # definitions的value
            self.c = print_instance.c
            self.print_instance = print_instance
            self.n = 0

        def get_define_obj(self,define):
            if define:
                define_value=''
                for i in define.split("/"):
                    if i == '#':
                        continue
                    elif i == "definitions":
                        continue
                    else:
                        define_value = self.definitions.get(i)
                return define_value
            else:
                return {}

        def get_definitions_params_dict(self,define):
            include_define_values = []
            definitions_model_param_dicts = []
            define_value = self.get_define_obj(define)
            params_dict = define_value.get("properties")
            if params_dict:
                for params_name, params_properties in params_dict.items():

                    params_desc = params_properties.get("description")
                    params_ref = params_properties.get("$ref")
                    params_type = params_properties.get("type")
                    params_properties['name'] = params_name
                    # 此处需要判断该参数的值是否为另外一个对象
                    definitions_model_param_dicts.append(params_properties)
                    if params_ref:
                        #  假如此处有另外一个定义的类,
                        include_define_values.append([params_ref,params_desc])  # 加入到后续需要打印的内部类list中,以便后面补打印
                        #  该参数仍然需要后续做testcase的打印,type为object,因此加入到返回结果列表中

                    elif params_type == "array":
                        # 加入此处是一个list类型
                        items = params_properties.get("items")  # 获取list类型的方法体
                        # if items.has_key("$ref"):
                        if "$ref" in items:
                            #  假如此处list中的item有另外一个定义的类,
                            # 加入到后续需要打印的内部类list中,以便后面补打印
                            if items.get('$ref') == define:
                                pass  #  此处出现自己引用自己的类不需要在打印用例
                            else:
                                include_define_values.append([items.get('$ref'),items.get('description')])
                    else:
                        pass

            # 判断是否有其他需要加入list结果中的对象(参数集合)
            if include_define_values:
                # include_define_values = list(set(include_define_values))
                for other_define in include_define_values:
                    params_ref = other_define[0]
                    params_desc = other_define[1]
                    result = self.get_definitions_params_dict(params_ref)
                    definitions_model_param_dicts.extend(result)
            return definitions_model_param_dicts

        def analyze_define(self, define, is_test_case=False):
            """
            打印definitions中的内容
            :param define:"#/definitions/优惠券批次DTO"
            :param is_test_case: 是否是打印testcase

            :return:
            """
            self.n +=1
            if self.n < 100:

                include_define_values = []
                define_value = self.get_define_obj(define)
                if define_value:
                    params_dict = define_value.get("properties")
                else:
                    params_dict = None
                # 如定义中properties为空，则不遍历
                if params_dict is not None:
                    for params_name, params_properties in params_dict.items():

                        params_desc = params_properties.get("description")
                        params_ref = params_properties.get("$ref")
                        params_type = params_properties.get("type")
                        # 此处需要判断该参数的值是否为另外一个对象
                        if params_ref:
                            #  假如此处有另外一个定义的类,
                            include_define_values.append([params_ref,params_desc])  # 加入到后续需要打印的内部类list中,以便后面补打印
                            #  则需要拼接另外一个类的类名,传入打印方法中
                            self.analyze_param(params_name, params_desc, default_value=self.get_obj_value(params_ref))
                        elif params_type == "array":
                            items = params_properties.get("items")  # 获取list类型的方法体
                            # if items.has_key("$ref"):
                            if "$ref" in items:
                                #  假如此处list中的item有另外一个定义的类,
                                # 加入到后续需要打印的内部类list中,以便后面补打印
                                # 此处需要解决自己引用自己的问题
                                if items.get('$ref') == define:
                                    pass  # 进入该条件说明该类有出现自己引用自己的情况,则不加入到后续打印列表中
                                else:
                                    include_define_values.append([items.get('$ref'),items.get('description')])

                                #  打印该key时默认值需要加上[]
                                self.analyze_param(params_name, params_desc, default_value='[' + self.get_obj_value(items.get("$ref")) + ']')
                            else:
                                #  todo 暂时未处理如果list类型中的item不是单独定义的一个define的情况又不是[1,2,3]这种类型的情况
                                self.analyze_param(params_name, params_desc, default_value=[])
                                #  该情况就是key=[1,2,4,5]的情况,值之后自己补充

                        else:
                            self.analyze_param(params_name, params_desc)

                # 判断是否有需要打印的内部类
                include_define_values = self.deal_duplicate(include_define_values)  #  去重
                if include_define_values:
                    # include_define_values = list(set(include_define_values))
                    for other_define in include_define_values:
                        self.c.write('\n')
                        self.c.dedent()  # {1}回到与def相同level的地方新建内部类
                        # print("=======开始打印类:" + self.get_sub_class_name(other_define[0]))
                        self.c.write("class {sub_class_name}(BaseObj):\n".format(
                                sub_class_name=self.get_sub_class_name(other_define[0])
                                # 见include_define_values.append([params_ref,params_desc])
                        ))  # 打印内部class的头
                        self.c.indent()  # 开始打印内部类init的方法体
                        self.c.write("\"\"\"{desc}\"\"\"\n".format(desc=other_define[1]))
                        # 见include_define_values.append([params_ref,params_desc])
                        self.c.write("def __init__(self):\n")
                        self.c.indent()  # 开始打印init内部的属性
                        self.c.write("super().__init__()\n")
                        self.analyze_define(other_define[0])
                        self.c.dedent()  # 结束打印init内部的属性
                        self.c.dedent()  # 结束打印内部类init的方法体
                        self.c.indent()  # 与内部类dedent匹配{1}


        def deal_duplicate(self, array):
            l_keys = []
            for index, l in enumerate(array):
                if l in l_keys:
                    array.pop(index)
                else:
                    l_keys.append(l)
            return array

        def get_obj_value(self,params_ref):
            return "self." + self.get_sub_class_name(params_ref) + "()"

        def get_sub_class_name(self,params_ref):
            class_name = params_ref.split('/')[2]  # todo 这里写死了index不太好
            class_name.replace('»','')
            class_name.replace('«','')
            class_name.replace('_','')
            class_name.replace('(','')
            class_name.replace(')','')
            # try:
            #     if self.is_chinese(class_name):
            #         class_name = "Defined"
            # except AttributeError as e:
            #     print(e)
            return class_name

        def is_chinese(self,s):

            """判断一个unicode是否是汉字"""

            # s = s.decode("utf-8")
            rt = False
            if s>= u"\u4e00" and s<= u"\u9fa6":
                rt = True
            return rt

        def analyze_param(self, params_name, params_desc, default_value=None):
            """
            打印参数和以参数为单位的内容
            :param params_name: 参数的名字
            :param params_desc: 参数的描述
            :param default_value: 参数的默认值
            :return:
            """
            # if default_value:
            #     print("打印的参数:" + params_name + "默认值值是:" + default_value)
            # else:
            #     print("打印的参数:" + params_name + "默认值值是:" + "None")
            self.c.write("self.{params_name} = {default_value}  # {params_desc}\n".format(params_name=params_name,
                                                                                          default_value=default_value,
                                                                                          params_desc=params_desc
                                                                                          ))



if __name__ == '__main__':
    # base_name为生成.py文件名称
    # http://192.168.170.22:8103/swagger-ui.html
    # p = Print(url='http://qanotify-wilson-base.intra.yeshj.com/v2/api-docs?group=PushAPI', base_name='abs_push_mee1')
    p = Print(url='http://qanotify-wilson.intra.yeshj.com/v2/api-docs?group=NodeAPI', base_name='abs_node')
    # p = Print(url='http://qaecm-tc-order.soa.yeshj.com/swagger.json', base_name='abs_push_xxx')

    # 关于测试模型生成的脚本信息如下:
    file_path = '/Users/songmengyun/automation_NC/business/bus_abs/'  # 文件目录的绝对路径, 最后生成的路径为：file_path+base_name
    # p.analyze_test_data(file_path=file_path)


    # 关于用例生成的脚本信息如下:
    case_path = '/Users/songmengyun/automation_NC/testcase/test_abs/'   # case目录的绝对路径
    p.print_test_case(file_path=case_path)


    # 1. 如果要调整生成用例的默认配置,请搜索方法名get_param_test_value进行修改,该方法是根据type和normal来生成正逆用例
    # 2. 打印某个接口下某个参数的用例方法print_the_api_only_param_test_case




