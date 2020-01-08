from model import CabbageModel
from controller import CabbageController as controller

import os
if __name__ == '__main__':
    #cabb = CabbageModel()
    #리눅스에서 돌아간다
    #모델이 존재하지 않을경우만 실행한다.
    print('d : 종목')
    print('e : 네이버 주가')
    flag = input('선택')
    call = controller()

    call.exec(flag)



    #if not os.path.exists('saved_model/checkpoint') and ( flag != 'e' and flag != 'd' ):
    #    cabb.create_model()