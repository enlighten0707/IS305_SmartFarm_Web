from django.shortcuts import render
from django.http import HttpResponse
import zipfile
from .test_maturity import get_maturity_rate
import numpy as np
import glob

# Create your views here.
def upload(request):
    '''
    上传图片并保存到当前目录下，便于后续处理；同时返回该图片数据，便于在页面上显示已经上传的图片
    '''
    file_list = request.FILES.getlist('file')
    file = file_list[0]
    img_dir = "./CropMaturity/Data/test_images.zip"
    data = file.file.read()

    with open(img_dir, 'wb') as f:
        f.write(data)
    
    with zipfile.ZipFile(img_dir) as zf:
        zf.extractall("./CropMaturity/Data")
    
    return HttpResponse("Upload Success")

    
def test_maturity(request):

    maturity_rate = get_maturity_rate("./CropMaturity/Data")
    maturity_rate = np.round(100*maturity_rate,2)

    return HttpResponse(maturity_rate)
