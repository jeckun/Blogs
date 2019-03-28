"""
使用第三方库pymupdf，实现Pdf转换png，在转换为Pdf，并完成压缩
https://pymupdf.readthedocs.io/en/latest/

使用举例：
python3 pdf2png.py xxxx.pdf 80
参数1： 要压缩的PDF文件
参数2： 压缩比例，按百分比
"""

import fitz
import os


class Pdf(object):
    __name__ = ''
    __path__ = ''
    __doc__ = None
    __totaling__ = ''

    def __init__(self, filename=None):
        if os.path.isfile(filename):
            self.__path__, self.__name__ = os.path.split(filename)
            self.__name__, __extention__ = os.path.splitext(self.__name__)

            if __extention__.lower() != '.pdf':
                raise TypeError('Not a PDF file.')
            self.__doc__ = fitz.open(filename)
            self.__totaling__ = self.__doc__.pageCount
        else:
            pass

    def to_png(self, path='.', compress=1.0):
        png_ls = []
        if not os.path.isdir(path):
            raise ValueError('No path was found.')
        for pg in range(self.__totaling__):
            page = self.__doc__[pg]
            # zoom = int(100)
            rotate = int(0)
            # trans = fitz.Matrix(zoom / 200.0, zoom / 200.0).preRotate(rotate)
            trans = fitz.Matrix(compress, compress).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            filename = os.path.join(self.__path__, ('%s.jpg' % (self.__name__+'_'+str(pg))))
            pm.writePNG(filename)
            png_ls.append(filename)
        return png_ls

    def from_png(self, pngs=[]):
        # 对图片文件列表进行排序
        # 图片文件命名规则：文件名_n.png
        def index(filename):
            name, exten = os.path.splitext(filename)
            return int(name.split('_')[1])

        # 检查文件是否存在
        for file in pngs:
            if not os.path.exists(file):
                raise TypeError('The document %s was not found.' % file)
            __name__, __extention__ = os.path.splitext(file)
            if __extention__.lower() not in ('.png','.jpg'):
                raise TypeError('Not a png file.')

        # 保存pdf文件)
        self.__doc__ = fitz.open()
        pngs.sort(key=index)
        for img in pngs:
            imgdoc = fitz.open(img)
            pdfbytes = imgdoc.convertToPDF()
            imgpdf = fitz.open("pdf", pdfbytes)
            self.__doc__.insertPDF(imgpdf)
            os.remove(img)
        filename = os.path.join(self.__path__, self.__name__+"_zip.pdf")
        if os.path.exists(filename):
            os.remove(filename)
        self.__doc__.save(filename)
        self.__doc__.close()

        return


