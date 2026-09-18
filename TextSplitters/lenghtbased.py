from langchain_text_splitters import CharacterTextSplitter

text="""Technology has changed the way people communicate, learn, and
solve problems. Every day, new ideas and tools are developed to make tasks faster and more efficient. However, technology is most useful when it is combined with creativity, critical thinking, and a clear understanding of real-world problems. Learning how different systems work and experimenting with new ideas can help people develop practical skills that remain valuable in a constantly changing world. The ability to adapt, learn from mistakes, and continuously improve is often more important than simply knowing a particular tool or technology.
"""

splitter=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_text(text)
print(result)