#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary==None:
        return None
    else:
         new=[]
         for i in a_dictionary:
               new.append(a_dictionary[i])
         new.sort()
         max=new[len(new)-1]
         for key in a_dictionary:
              if max==a_dictionary[key]:
                   return key
              




#a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
#best_score(a_dictionary)                        