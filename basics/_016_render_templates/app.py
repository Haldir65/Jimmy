from jinja2 import Environment, FileSystemLoader
import configparser
import os, sys

tamplate_dir = './tpl'
output_dir = './output/'
config_file = "server_config.ini"

#判断文件夹是否存在，不存在则创建
def chk_mkdir(dirname):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

#从ini文件中读取配置
def load_config(server_name):
    cf = configparser.ConfigParser()
    cf.read(config_file)
    values = cf.items(server_name)
    return values

#用jinja渲染模板生成最终配置文件的主函数
def render_to_file(server_name):
    env = Environment(loader = FileSystemLoader(tamplate_dir))
    tpl_list = os.listdir(tamplate_dir)
    # 渲染tpl目录下的所有模板
    for t in tpl_list:
        tpl = env.get_template(t)
        info = load_config(server_name)
        output = tpl.render(info)
        with open(output_dir + t+'.json', 'w') as out:
            out.write(output)


if __name__ == "__main__":
    server_name = sys.argv[1]
    chk_mkdir(output_dir)
    render_to_file(server_name)
