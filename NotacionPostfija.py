from pythonds.basic.stack import Stack

def infijoAPostfijo(regex):
    prec = {}
    prec["*"] = 2
    prec["|"] = 2
    prec["+"] = 2
    prec["?"] = 2
    prec["."] = 2
    prec["("] = 1
    opStack = Stack()
    if regex[1] == '(':
      regex = regex
    else:
      regex = '(' + regex + ')'
    ListaPost = []
    ListaTokens = [x for x in list(regex) if x not in (' ')]
    Metacaracteres=["*", "|", "|", "+", "?", "."]
    
    for token in ListaTokens:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            ListaPost.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                ListaPost.append(topToken)
                ListaPost.append('.')
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  ListaPost.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        ListaPost.append(opStack.pop())
    return " ".join(ListaPost)


print infijoAPostfijo("(ab*)*c")
