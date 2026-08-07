from utils.rag import ask_rag


question = "Where did I spend the most money?"


answer = ask_rag(question)


print("\nFINWISE AI RESPONSE")
print("-------------------")
print(answer)