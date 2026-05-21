from google import genai
client = genai.Client()

def size(s):
    if s==1:
        return 10
    elif s==2:
        return 25
    elif s==3:
        return 60
    raise ValueError("Enter 1 or 2 or 3 only") 

def summarize(txt,p): 
    if txt.strip()=="":
        raise ValueError("Empty text")
    response = client.models.generate_content(
                model="gemini-3-flash-preview", contents=f"Summarize the following content to a size of {p}% of original content (strictly): {txt}"
            )
    summmary=response.text
    return summmary

def keywordize(txt):
    if txt.strip()=="":
        raise ValueError("Empty text")
    response = client.models.generate_content(
                model="gemini-3-flash-preview", contents=f"Go through the following content and give comma separated key words (format: keyword1, keyword2, ... ) :{txt}"
            )
    keywordsresp= response.text
    keywords = keywordsresp.replace(", ","\n")
    return keywords

def main():
    inputF= input("Enter your file path here: ")
    try:
        with open(inputF) as f:
            txt= f.read()
            s= int(input("How do you want the summary to be :\n  1.Small\n  2.Medium\n  3.Long\n  choice: "))
            p =  size(s)
            summary = summarize(txt,p)
            keywords = keywordize(txt)
            with open("Response.txt","w") as f2:
                f2.write(f"---------SUMMARY--------\n{summary}\n\n---------KEYWORDS--------\n{keywords}") 
                print("OK done!")
    except FileNotFoundError:
        print("Error : Failed to find file")
    except ValueError as e:
        print(f"Error : {str(e)}")
    except Exception as e:
        print("Error : ",e)

if __name__=="__main__":
    main()


