from scipy import optimize as opt
from scipy import stats as stats
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import numpy as np
import math

def gen_entropy(entropy,length,precision='1.0000',seed=None):
    """
    gen_entropy(entropy, length, precision='1.0000', seed=None)

    Generate a list of length 'length' of values in the range [0,1] which
    have an entropy of 'entropy'. The entropy of the generated list will be as close
    as possible to the specified entropy. The precision of the generated list values
    can be set using the optional 'precision' parameter (default value is '1.0000').
    The random number generator seed can be set using the optional 'seed' parameter.

    Parameters:
    - entropy: float
        The target entropy for the generated list. It must be in the interval [0,log2(length)].
    - length: int
        The length of the list to be generated.
    - precision: str (optional, default='1.0000')
        The number of decimal places to round the generated list values to.
    - seed: int or None (optional, default=None)
        The seed for the random number generator. If None, a new seed will be generated
        each time the function is called.

    Returns:
    - list_q: list of float
        A list of length 'length' of values in the range [0,1] with the specified entropy.
        Each value is rounded to the specified precision.

    Raises:
    - ValueError: If the specified entropy is not in the interval [0,log2(length)].
    """
    def entropy_minus_one(ent,q):
        x = ent - ((-q * math.log(q,2)) - ((1-q) * math.log(1-q,2)))
        return x/(1-q)

    list_q = []
    list_p = [0] * length
    list_b = []
    rng = np.random.default_rng(seed=seed)

    if entropy > math.log(length,2):
        raise ValueError('Entropy must be in interval [0;log2(length)] !')

    temp_ent = entropy
    index_q = 0
    for i in range(length,2,-1):
        def entropy_log(q):
            return entropy_minus_one(temp_ent, q) - math.log(i - 1, 2)
        def entropy_normal(q):
            return entropy_minus_one(temp_ent, q)

        if temp_ent >= 1 and temp_ent <= math.log(i-1,2):
            j = rng.uniform(2**(-temp_ent),1)
            while(True):
                if(entropy_minus_one(temp_ent,j) <= math.log(i - 1, 2)):
                    j = rng.uniform(j,1)
                else:
                    g = j
                    break
            
            sol = opt.root_scalar(entropy_log,bracket=[2**(-temp_ent),g],method='toms748')
            a = float(D(sol.root).quantize(D(precision),rounding=ROUND_DOWN))

            list_b.append((0,a))
            list_q.append(float(D(rng.uniform(0,a)).quantize(D(precision))))

        elif temp_ent > math.log(i-1,2):
            j = rng.uniform(0,2**(-temp_ent))
            while(True):
                if(entropy_minus_one(temp_ent,j) <= math.log(i - 1, 2)):
                    j = rng.uniform(0,j)
                else:
                    g1 = j
                    break

            j = rng.uniform(2**(-temp_ent),1)
            while(True):
                if(entropy_minus_one(temp_ent,j) <= math.log(i - 1, 2)):
                    j = rng.uniform(j,1)
                else:
                    g2 = j
                    break

            sol = opt.root_scalar(entropy_log,bracket=[g1,2**(-temp_ent)],method='toms748')
            a = float(D(sol.root).quantize(D(precision),rounding=ROUND_UP))
            sol = opt.root_scalar(entropy_log,bracket=[2**(-temp_ent),g2],method='toms748')
            b = float(D(sol.root).quantize(D(precision),rounding=ROUND_DOWN))

            list_b.append((a,b))
            list_q.append(float(D(rng.uniform(a,b)).quantize(D(precision))))

        elif temp_ent < 1:
            j = rng.uniform(0,2**(-temp_ent))
            while(True):
                if(entropy_minus_one(temp_ent,j) <= 0):
                    j = rng.uniform(0,j)
                else:
                    g1 = j
                    break

            j = rng.uniform(2**(-temp_ent),1)
            while(True):
                if(entropy_minus_one(temp_ent,j) <= 0):
                    j = rng.uniform(j,1)
                else:
                    g2 = j
                    break

            j = rng.uniform(2**(-temp_ent),1)
            while(True):
                if(entropy_minus_one(temp_ent,j) <= math.log(i - 1, 2)):
                    j = rng.uniform(j,1)
                else:
                    g3 = j
                    break

            sol = opt.root_scalar(entropy_normal,bracket=[g1,2**(-temp_ent)],method='toms748')
            a = float(D(sol.root).quantize(D(precision),rounding=ROUND_DOWN))
            sol = opt.root_scalar(entropy_normal,bracket=[2**(-temp_ent),g2],method='toms748')
            b = float(D(sol.root).quantize(D(precision),rounding=ROUND_UP))
            sol = opt.root_scalar(entropy_log,bracket=[2**(-temp_ent),g3],method='toms748')
            c = float(D(sol.root).quantize(D(precision),rounding=ROUND_DOWN))

            if rng.integers(1,3) == 1:
                list_b.append((0,a))
                list_q.append(float(D(rng.uniform(0,a)).quantize(D(precision))))
            else:
                list_b.append((b,c))
                list_q.append(float(D(rng.uniform(b,c)).quantize(D(precision))))
        
        if(length > 2):
            temp_ent = float(D(entropy_minus_one(temp_ent,list_q[index_q])).quantize(D(precision),rounding=ROUND_DOWN))
            index_q += 1

    last_ent = temp_ent

    def entropy_binary(q):
        return -q*math.log(q,2) - (1-q)*math.log(1-q,2) - last_ent

    j = rng.uniform(0,0.5)
    while(True):
        if(entropy_binary(j) >= 0):
            j = rng.uniform(0,j)
        else:
            g1 = j
            break

    j = rng.uniform(0.5,1)
    while(True):
        if(entropy_binary(j) >= 0):
            j = rng.uniform(j,1)
        else:
            g2 = j
            break

    sol = opt.root_scalar(entropy_binary,bracket=[g1,0.5],method='toms748')
    list_q.append(sol.root)
    sol = opt.root_scalar(entropy_binary,bracket=[0.5,g2],method='toms748')
    list_q.append(sol.root)

    x = 1
    for i in range(0,length-2):
        list_p[i] = c = float(D(list_q[i]*x).quantize(D(precision)))
        x = x - list_p[i]
    list_p[length-2] = float(D(list_q[length-2]*x).quantize(D(precision)))
    list_p[length-1] = float(D(list_q[length-1]*x).quantize(D(precision)))

    return list_p