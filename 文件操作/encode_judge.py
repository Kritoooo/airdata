from chardet import UniversalDetector

def get_encode_info(file):
    """
    逐个读取文件的编码方式
    """
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']
