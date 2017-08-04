class HtmlOutPuter():
    def __init__(self):
        self.data = []
    def output_html(self, direction=""):
        if(direction.find(".html") == -1):
            direction += 'output.html'
        with open(direction, 'w', encoding='utf-8') as fp:
            fp.write('<html>')
            fp.write("<meta charset='UTF-8'>")
            fp.write("<body>")    
            
            for ele in self.data:
                comments = {}
                for name,comments in ele.items():
                    fp.write("<h1>%s</h1>" % name)
                    for user,comment in comments.items():
                        fp.write("<p>%s : %s</p>" % (user, comment))
                    fp.write("<br>")
            
            fp.write("</body>") 
            fp.write('</html>')
            fp.close()
    def collect_datas(self, datas):
        if datas is None:
            return
        self.data.append(datas)