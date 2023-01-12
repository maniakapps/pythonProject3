from Crypto.Random import get_random_bytes
import Crypto.Util as crypto


class SocialistMillionaire:
    """
    This class implements the socialist millionaire problem.
    """

    def __init__(self, x, p, h, user_a=True):
        """
        Initializes class attributes.
        * Parameter x: fortune of this millionaire
        * Parameter p: prime number
        * Parameter h: value in Zp
        * Parameter user_a: True if user is Alice, False if it's Bob
        """
        # --- IMPLEMENTATION GOES HERE ---

        # --------------------------------
        self.x = x
        self.p = p
        self.h = h
        self.user_a = user_a
        if self.user_a:
            self.v = crypto.number.getRandomNBitInteger(192 * 8)
            self.w = crypto.number.getRandomNBitInteger(192 * 8)
        else:
            self.v = crypto.number.getRandomNBitInteger(192 * 8)
            self.w = crypto.number.getRandomNBitInteger(192 * 8)

    def steps_1_2(self):
        """
            Implements steps 1 and 2 of the socialist millionaire protocol
            * Returns: two element list with h values ([h^v, h^w])
        """
        result = []
        # --- IMPLEMENTATION GOES HERE ---
        result.append(pow(self.h, self.v) % self.p)
        result.append(pow(self.h, self.w) % self.p)
        # --------------------------------
        return result

    def steps_5_6_7_8(self, hvalues):
        """
        # Implements steps 5-8 of the socialist millionaire protocol
        # * Parameter hvalues: list with two elements, [h^v, h^w]
        # * Returns: two element list with [P_own, Q_own]
        """
        result = []
        # --- IMPLEMENTATION GOES HERE ---
        if self.user_a:
            res1 = pow(self.h, hvalues[0])
            res2 = pow(self.h, hvalues[1])
        # --------------------------------

        # step 6
        g = ()
        return result

    def steps_11_12(self, pqvalues):
        """
        # Implements steps 11-12 of the socialist millionaire protocol
        # * Parameter pqvalues: list with two values, Pcounter and Qcounter (received from the other party)
        # * Returns: product of Q values (inverting one of them first)
        """
        result = None
        # --- IMPLEMENTATION GOES HERE ---

        # --------------------------------
        return result

    def steps_15_16(self, qsprod):
        """
        # Implements steps 15-16 of the socialist millionaire protocol
        # * Parameter qsprod: the product of Q values received from the other party
        # * Returns: boolean, True if both users are equally rich
        """
        result = None
        # --- IMPLEMENTATION GOES HERE ---

        # --------------------------------
        return result