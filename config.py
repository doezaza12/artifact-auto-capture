import json
import os
class Configuration:
    save_img_path = os.getcwd()
    save_annotation_path = os.getcwd()
    template_img_path = os.path.join(os.getcwd(), 'template.jpg')

    @staticmethod
    def setSaveImagePath(save_img_path=save_img_path):
        if not os.path.exists(save_img_path):
            os.mkdir(save_img_path)
        Configuration.save_img_path = save_img_path

    @staticmethod
    def getSaveImagePath():
        return Configuration.save_img_path

    @staticmethod
    def setTemplateImagePath(template_img_path=template_img_path):
        if not os.path.exists(template_img_path):
            raise FileNotFoundError()
        Configuration.template_img_path = template_img_path

    @staticmethod
    def getTemplateImagePath():
        return Configuration.template_img_path

    @staticmethod
    def setSaveAnnotationPath(save_annotation_path=save_annotation_path):
        if not os.path.exists(save_annotation_path):
            os.mkdir(save_annotation_path)
        Configuration.save_annotation_path = save_annotation_path

    @staticmethod
    def getSaveAnnotationPath():
        return Configuration.save_annotation_path
