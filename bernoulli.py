import math
#Dictionary of the coefficient of each r
dict = {
  "0": [[1,1]],
  "1": [[-1,2], [1,1]]
}

B = dict.copy()
#Constant
con = [
  [0,1],
  [0,1],
  [1, 6],
  [0, 1],
  [1, 90],
  [0, 1],
  [1, 945],
  [0,1],
  [1, 9450],
  [0,1],
  [1, 93555],
  [0, 1],
  [691, 638512875]
]

def main():
  minus = False
  cnt = 0
  for n in range(2,13):
    if cnt == 2:
      cnt = 0
      minus = not minus
      
    cnt += 1
    dict[f"{n}"] = []
    B[f"{n}"] = []
    factorial = math.factorial(n)
    for k in range(len(dict[f"{n-1}"])+1):
      p = q = 1
      
      if k == 0:
        p = con[n][0]
        q = con[n][1] * math.pow(2, n-1)
        if minus:
          p *= -1
      elif k == 1:
        p = dict[f"{n-1}"][k-1][0] 
        q = dict[f"{n-1}"][k-1][1]
      else:
        p = dict[f"{n-1}"][k-1][0]
        q = k*dict[f"{n-1}"][k-1][1]
      
      dict[f"{n}"].append([int(p), int(q)])
         
      p *= factorial
      
      #Irreducible fractionl
      gcd = math.gcd(int(p), int(q))
      if gcd != 1:
        p = p / gcd 
        q = q / gcd
      
      B[f"{n}"].append([int(p), int(q)])

  #output
  for i in range(len(B)):
    print("{}: ".format(i), end="")
    for j in range(len(B[f"{i}"])):
      print(B[f"{i}"][len(B[f"{i}"])-1-j], end=" ")
    print()

  return
  
if __name__=="__main__":
  main()