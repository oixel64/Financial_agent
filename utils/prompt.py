class Prompt:
    # 意图识别提示词
    def create_ir_icl_prompt(user_question):
        prompt = """你是一个智能助手，请谨记你的工作要求，：
对于每个提供给你的问题，只属于一类，类别不是文本理解就是数据查询。你需要遵循下面的步骤进行工作：
1. 先确定问题的类别。
2. 根据类别判断是否需要进行公司名称与关键词识别，若为数据查询类问题，不需要进行公司名称与关键词识别，输出"数据查询，公司名称：“”,关键词：“”"。
若为文本理解类问题，输出"文本理解，公司名称：“xxx”,关键词：“xxx”"

下面是数据查询可供使用的表和字段信息：
    字段：基金代码, 基金全称, 基金简称, 管理人, 托管人, 基金类型, 成立日期, 到期日期, 管理费率, 托管费率, 持仓日期, 股票代码, 股票名称, 数量, 市值, 市值占基金资产净值比, 第N大重仓股, 所在证券市场, 所属国家(地区), 报告类型, 债券类型, 债券名称, 持债数量, 持债市值, 持债市值占基金资产净值比, 对应股票代码, 交易日期, 单位净值, 复权单位净值, 累计单位净值, 资产净值, 昨收盘(元), 今开盘(元), 最高价(元), 最低价(元), 收盘价(元), 成交量(股), 成交金额(元), 行业划分标准, 一级行业名称, 二级行业名称, 公告日期, 截止日期, 报告期期初基金总份额, 报告期基金总申购份额, 报告期基金总赎回份额, 报告期期末基金总份额, 定期报告所属年度, 机构投资者持有的基金份额, 机构投资者持有的基金份额占总份额比例, 个人投资者持有的基金份额, 个人投资者持有的基金份额占总份额比例
    表名：基金基本信息、基金股票持仓明细、基金债券持仓明细、基金可转债持仓明细、基金日行情表、A股票日行情表、港股票日行情表、A股公司行业划分表、基金规模变动表、基金份额持有人结构

下面是一些例子：
    问题：“在2019年的中期报告里，XX基金管理有限公司管理的基金中，有多少比例的基金是个人投资者持有的份额超过机构投资者？希望得到一个精确到两位小数的百分比。”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“XXXX股份有限公司变更设立时作为发起人的法人有哪些？”
    回答：“文本理解，公司名称：“XXXX股份有限公司”,关键词：“变更设立时作为发起人的法人””
    
    问题：“我想知道XXXXXX债券A基金在20200930的季报中，其可转债持仓占比最大的是哪个行业？用申万一级行业来统计。”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“XXXXXX股份有限公司2020年增资后的投后估值是多少？”
    回答：“文本理解，公司名称：“XXXXXX股份有限公司”,关键词：“2020年增资后的投后估值””
    
    问题：“根据XXXXXX股份有限公司招股意向书，全球率先整体用LED路灯替换传统路灯的案例是？”
    回答：“文本理解，公司名称：“XXXXXX股份有限公司”,关键词：“全球率先整体用LED路灯替换传统路灯的案例””
    
    问题：“什么公司、在何时与XXXXXX股份有限公司发生了产品争议事项？产品争议事项是否已经解决？”
    回答：“文本理解，公司名称：“XXXXXX股份有限公司”,关键词：“什么公司、在何时发生了产品争议事项？产品争议事项是否已经解决？””
    
    问题：“请帮我查询下股票代码为XXXXXX的股票在2021年内最高日收盘价是多少？”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“XXXXXX股份有限公司的中标里程覆盖率为多少？”
    回答：“文本理解，公司名称：“XXXXXX股份有限公司”,关键词：“中标里程覆盖率””
    
    问题：“根据中国证监会颁布的《上市公司行业分类指导》的规定，XXXXXX有限公司所属的行业大类、中类、小类是什么？”
    回答：“文本理解，公司名称：“XXXXXX有限公司”,关键词：“行业大类、中类、小类””
    
    问题：“请问XXXX年一季度有多少家基金是净申购?它们的净申购份额加起来是多少?请四舍五入保留小数点两位。”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“XXXXXX有限公司和合肥翰林是否按规定为员工缴纳了社会保险？”
    回答：“文本理解，公司名称：“XXXXXX有限公司、合肥翰林”,关键词：“为员工缴纳社会保险””
    
    问题：“我想知道XXXXXX有限公司在2020年成立了多少只管理费率小于0.8%的基金？”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“根据《CRCC产品认证实施规则》，《铁路产品认证证书》有效期为多久？XXXXXX有限公司取得 《铁路产品认证证书》后，至少多久需要接受一次监督？”
    回答：“文本理解，公司名称：“XXXXXX有限公司”,关键词：“取得 《铁路产品认证证书》后，至少多久需要接受一次监督””
    
    问题：“我想知道XXXXXX基金管理有限公司在2019年成立了多少只管理费率小于0.8%的基金？”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“请问XXXX年一季度有多少家基金是净申购?它们的净申购份额加起来是多少?请四舍五入保留小数点两位。”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“我想知道XXXXXX有限公司在2019年成立了多少只管理费率小于0.8%的基金？”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“我想知道股票XXXXXX在申万行业分类下的二级行业是什么？用最新的数据。”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“请帮我查询下股票代码为XXXXXX的股票在2019年内最高日收盘价是多少？”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“股票XXXXXX在20200227日期中的收盘价是多少?（小数点保留3位）”
    回答：“数据查询，公司名称：“”,关键词：“””
    
    问题：“截至2009年底，中海达、南方测绘合计占有国产品牌销售额的多大比例？”
    回答：“文本理解，公司名称：“中海达、南方测绘”,关键词：“占有国产品牌销售额的比例””
    
    问题：“截止2005年12月31日，南岭化工厂的总资产和净资产分别是多少？”
    回答：“文本理解，公司名称：“南岭化工厂”,关键词：“总资产和净资产””
    
    问题：“股票XXXXXX在20200227日期中的收盘价是多少?（小数点保留3位）”
    回答：“数据查询，公司名称：“”,关键词：“””

    根据上面提供的例子和信息对以下问题进行分类。
"""
        
        # 添加用户问题部分
        prompt += f"问题：\"{user_question}\"\n回答:\""
        
        return prompt

    # sql icl 提示词
    def create_sql_icl_prompt(user_question, exps):
        # 模板头部
        prompt_template = "将下面的问题转化为SQL语句。\n可供使用的表和字段信息：\n字段：基金代码, 基金全称, 基金简称, 管理人, 托管人, 基金类型, 成立日期, 到期日期, 管理费率, 托管费率, 持仓日期, 股票代码, 股票名称, 数量, 市值, 市值占基金资产净值比, 第N大重仓股, 所在证券市场, 所属国家(地区), 报告类型, 债券类型, 债券名称, 持债数量, 持债市值, 持债市值占基金资产净值比, 对应股票代码, 交易日期, 单位净值, 复权单位净值, 累计单位净值, 资产净值, 昨收盘(元), 今开盘(元), 最高价(元), 最低价(元), 收盘价(元), 成交量(股), 成交金额(元), 行业划分标准, 一级行业名称, 二级行业名称, 公告日期, 截止日期, 报告期期初基金总份额, 报告期基金总申购份额, 报告期基金总赎回份额, 报告期期末基金总份额, 定期报告所属年度, 机构投资者持有的基金份额, 机构投资者持有的基金份额占总份额比例, 个人投资者持有的基金份额, 个人投资者持有的基金份额占总份额比例\n表名：基金基本信息、基金股票持仓明细、基金债券持仓明细、基金可转债持仓明细、基金日行情表、A股票日行情表、港股票日行情表、A股公司行业划分表、基金规模变动表、基金份额持有人结构\n\n下面是一些例子。\n\n"
        
        # 添加找到的样本问题和对应的SQL语句
        for question, sql in exps:
            prompt_template += f"对于问题：\"{question}\"\n你应该回答：{sql}\n\n"
        
        # 添加用户问题部分
        prompt_template += f"对于问题：\"{user_question}\"\n你应该回答：\n"
        
        return prompt_template

    # sql最后合并结果提示词
    def create_final_icl_prompt(new_question, query_result, exps):
        q_exps, query_result_exps, final_response_exps = zip(*exps)
        prompt_head = """
你是一个可以整合问题和答案为完整的一句话的智能助手，你可以进行小数点保留与取整操作。
我会给你一个问题以及该问题的回答（回答是sql的查询结果）。请你按照下面的要求进行整合输出：
首先你需要根据问题去正确提取sql输出中的答案，然后总结到一起成为一句通顺的语句输出，不要输出任何多余的说明。下面是一些例子：\n
"""
        for q_exp, query_result_exp, final_reposon_exp in zip(q_exps, query_result_exps, final_response_exps):
            prompt_head += f"用户提问：{q_exp}\nsql查询结果：{query_result_exp}\n你的回答：{final_reposon_exp}\n\n"
        
        prompt_head += f"用户提问：{new_question}\nsql查询结果：{query_result}\n你的回答：\n\n"

        return prompt_head
    
    # 文本理解最后合并结果提示词
    def create_final_text_prompt(new_question, contents):
        # 拼接所有文档内容
        content_str = "\n\n".join(contents)
        
        # 创建提示
        prompt = f"""
您是文档问答系统高级专家。根据以下原则、步骤及示例，您可以通过在文档中查找相关内容并仿造示例进行输出:

原则:
1、输出一定在提供的文档内容中，且只能根据提供的文档内容来回答问题
2、直接回答问题，不需要列出中间的思考过程，不需要拓展
3、同一个问题，文本中有不同的答案，需要综合起来回答
4、问题答案在文档中是分点/条、系列措施时列举时，需要全部列出不遗漏;
5、文本中数值与两边的文字可能有空格或换行符，与没有这两类的符号的含义是相同的。例如"持有8926万股”与"持有 8926 万股"、"持有 8926万股"、"持有 8926\n万股"含义是相同的
6、无需摘录原文

步骤:
1、判断下面问题中是否有多个问题，若存在多个问题，将问题拆分出多个问题;
2、根据拆分出来的问题，精确定位文档中的内容，可能存在一个或多个位置，存在多个时需要都找出来;
3、根据定位出来的位置前后内容，回答每个问题;
4、优先根据文档原文来回答每个问题;若没有，再概况总结回答

示例
下面将提供示例文档内容、问题及输出，仿照样例输出
示例1文档内容:惠州光弘科技股份有限公司，报告期内2014年、2015年、2016年和2017年1-6月份客户供料、非客户供料合作模式下营业成本构成及占比变动情况。客户供料模式下材料成本比重分别为\n13.15%、12.69%、13.38%和11,40%，\n人工成本比重分别为56,88%、58.17%、54,71%和51.52%，制造费用比重分别为29.97%、29.14%、31.91%和37.08%,比例结构稳定;非客户供料模式下，材料成本比重分别为81.55%、85.69%91.33%和\n90.17%。该业务模式下，其生产制造所需主要物料由发行人自行采购，按照产品整机的销售价格收取产品销售费，因此其材料成本占比较高
示例1问题:报告期内，2016年惠州光弘科技股份有限公司非客户供料模式下材料成本比重?
示例1输出:报告期内，2016年惠州光弘科技股份有限公司非客户供料模式下材料成本比重91.33%

文档内容:\n{content_str}\n
问题:{new_question}
        """
        
        return prompt

