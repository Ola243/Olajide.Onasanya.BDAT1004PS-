from html.parser import HTMLParser


class HeadingParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        self.curr = None

        super().__init__(convert_charrefs=convert_charrefs)

    def handle_starttag(self, tag, attrs):
        self.curr = tag

    def handle_data(self, data):
        data = data.replace("\t", '', -1)
        data = data.replace(" ", '', -1)
        data = data.replace("\n", '', -1)
        data = "".join([w for w in data.split("\n") if w != ''])

        if len(data) == 0:
            return

        if self.curr == "h1":
            print(data)
        elif self.curr == "h2":
            print(f" {data}")
        elif self.curr == "h3":
            print(f"  {data}")
        elif self.curr == "h4":
            print(f"   {data}")
        elif self.curr == "h5":
            print(f"    {data}")
        elif self.curr == "h6":
            print(f"     {data}")
