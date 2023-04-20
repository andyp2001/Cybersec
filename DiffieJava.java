import java.math.BigInteger;

class DiffieJava {
  public static void main(String[] args) {


    //int p = 0x00fb2e8473c499d184d806e6b5df7f621b;

    //int alice = 0x2ca50afea541f0d90f68e0efc85c2686;

    //int bob = 0x6e146d3b2149f41450713e5c83d21e70;
    
    String p = "00fb2e8473c499d184d806e6b5df7f621b";
    String aliceHex = "2ca50afea541f0d90f68e0efc85c2686";
    String bobHex = "6e146d3b2149f41450713e5c83d21e70";

    //Alice and Bob agree on a prime number p and a generator g. Both of these values are public.
    
    //coverting to bigintegers
    BigInteger P = new BigInteger(p, 16);
    BigInteger alice = new BigInteger(aliceHex, 16);
    BigInteger bob = new BigInteger(bobHex, 16);
    BigInteger g = new BigInteger("2");

    //getting the bit count of P
    int bitCount = P.bitLength();

    //Alice chooses a secret number a and calculates A = g^a mod p. She sends A to Bob.
    BigInteger A = g.modPow(alice, P); // Calculate g^a mod p

    //Bob chooses a secret number b and calculates B = g^b mod p. He sends B to Alice.
    BigInteger B = g.modPow(bob, P); // Calculate g^b mod p

    //Alice calculates s = B^a mod p, while Bob calculates s = A^b mod p. Both Alice and Bob now have the same secret key s, which they can use for secure communication. 
    BigInteger secretA = A.modPow(bob, P); 
    String HexA = secretA.toString(16);

    BigInteger secretB = B.modPow(alice, P); 
    String HexB = secretB.toString(16);


    /*
Your program must print the following output:

Bit count of p: 128
Shared key A  : 587b4f3e8914f86c63af504c3b42750c
Shared key B  : 587b4f3e8914f86c63af504c3b42750c
  */
    
    System.out.println("Bit count of p: " + bitCount);
    System.out.println("Shared key A : " + HexA);
    System.out.println("Shared key B : " + HexB);

    
  }
}