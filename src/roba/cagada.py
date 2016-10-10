'''
Created on 10/10/2016

@author: ernesto
'''
import array
import logging

logger_cagada = None
nivel_log = logging.ERROR
nivel_log = logging.DEBUG

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return self.roba_caca_core(nums)
    
        
    def roba_caca_core(self, numeros):
        maximo_robo = 0
        toma_que_toma = array.array("L")
        no_toma = array.array("L")
        
                
        if(not numeros):
            return 0
        
        
        toma_que_toma.append(numeros[0])
        no_toma.append(0)
        
        for idx_num, numero in enumerate(numeros[1:],1):
	    logger_cagada.debug("fedewolf %u, anterior %u"%(idx_num,idx_num-1))
	    logger_cagada.debug("toma anterior %u, no toma anterior %u, num act %u"%(toma_que_toma[idx_num - 1],  no_toma[idx_num - 1], numero))
            no_toma.append(max([toma_que_toma[idx_num - 1], no_toma[idx_num - 1]]))
            toma_que_toma.append(no_toma[idx_num-1] + numero)
            
        logger_cagada.debug("toma que toma %s" % toma_que_toma)
        logger_cagada.debug("no toma %s" % no_toma)
        
        
        maximo_robo = max([toma_que_toma[-1], no_toma[-1]])
        logger_cagada.debug("el max beneficio %u" % maximo_robo)
        
        return maximo_robo
        

if __name__ == '__main__':
    parser = None
    args = None
    
    

    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    mierda=Solution()
#    mierda.rob([423,5,6,0,3,5,2,123,332])
#    mierda.rob([1,1])
    mierda.rob([1,3,1])
