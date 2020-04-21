from PySide2 import QtWidgets
import markdown

def viewInMarkdown(md,extensions,markdownView):
    html = mdToHtml(md,extensions)
    markdownView.setHtml(html)

def mdToHtml(md, extensions):
    html = markdown.markdown(md, extensions = extensions)
    return html