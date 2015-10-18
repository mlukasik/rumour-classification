'''
Created on 18 Oct 2015

@author: michal

Seeds for the random number generator from numpy for the ICM methods.
'''

def getseed(foldtorun, methodname, train_set_ratio):
    seed=None
    foldtorun=int(foldtorun)
    train_set_ratio=int(train_set_ratio)
    if foldtorun==0 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433794857
    if foldtorun==2 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795002
    if foldtorun==6 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795345
    if foldtorun==5 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795258
    if foldtorun==5 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795239
    if foldtorun==1 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433794893
    if foldtorun==5 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795248
    if foldtorun==1 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433794893
    if foldtorun==6 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795345
    if foldtorun==1 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433794893
    if foldtorun==4 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795170
    if foldtorun==4 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795181
    if foldtorun==2 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433794992
    if foldtorun==6 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795346
    if foldtorun==1 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433794893
    if foldtorun==3 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795093
    if foldtorun==3 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795092
    if foldtorun==3 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795070
    if foldtorun==6 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795355
    if foldtorun==4 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795170
    if foldtorun==5 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795258
    if foldtorun==2 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433794991
    if foldtorun==0 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433794855
    if foldtorun==2 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433794981
    if foldtorun==0 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433794846
    if foldtorun==4 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795180
    if foldtorun==2 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433794982
    if foldtorun==3 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795093
    if foldtorun==0 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433794857
    if foldtorun==4 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795180
    if foldtorun==5 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795240
    if foldtorun==3 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795092
    if foldtorun==6 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795345
    if foldtorun==0 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433794857
    if foldtorun==1 and methodname=="BOWGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433794894
    if foldtorun==0 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795425
    if foldtorun==2 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795529
    if foldtorun==6 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795892
    if foldtorun==5 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795795
    if foldtorun==5 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795795
    if foldtorun==1 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795469
    if foldtorun==5 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795795
    if foldtorun==1 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795468
    if foldtorun==6 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795891
    if foldtorun==1 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795468
    if foldtorun==4 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795694
    if foldtorun==4 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795694
    if foldtorun==2 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795528
    if foldtorun==6 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795875
    if foldtorun==1 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795468
    if foldtorun==3 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795612
    if foldtorun==3 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795612
    if foldtorun==3 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795611
    if foldtorun==6 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795892
    if foldtorun==4 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795694
    if foldtorun==5 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795794
    if foldtorun==2 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795529
    if foldtorun==0 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795426
    if foldtorun==2 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795529
    if foldtorun==0 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795426
    if foldtorun==4 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==30:
        seed=1433795693
    if foldtorun==2 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795528
    if foldtorun==3 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==50:
        seed=1433795621
    if foldtorun==0 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795418
    if foldtorun==4 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795694
    if foldtorun==5 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==10:
        seed=1433795783
    if foldtorun==3 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795611
    if foldtorun==6 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795891
    if foldtorun==0 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==20:
        seed=1433795417
    if foldtorun==1 and methodname=="BROWNGPjoinedfeaturesICMLIN" and train_set_ratio==40:
        seed=1433795469
    return seed