from langchain.text_splitter import CharacterTextSplitter


text = """
Pulsars are rapidly rotating neutron stars that emit beams of electromagnetic radiation from their magnetic poles. These beams sweep across space like lighthouse beams, and when aligned with Earth, they can be detected as periodic pulses—hence the name "pulsar."

First discovered in 1967 by Jocelyn Bell Burnell and Antony Hewish, pulsars have since fascinated astronomers for their extreme physical properties. A typical pulsar has a mass greater than that of the Sun, compressed into a sphere just about 20 kilometers in diameter. This incredible density results in surface gravity so strong that it warps spacetime.

There are several types of pulsars, including millisecond pulsars, which spin hundreds of times per second, and magnetars, which have incredibly strong magnetic fields. Pulsars serve as natural cosmic clocks due to their highly regular rotational periods. Scientists have even proposed using millisecond pulsars to create a galactic-scale GPS system for spacecraft navigation.

Interestingly, some pulsars are part of binary systems and can siphon matter from their companion stars. This transfer of mass can spin the pulsar up, resulting in the extremely rapid rotation observed in recycled or spun-up millisecond pulsars.

Beyond their use in astrophysical studies, pulsars also provide critical tests for general relativity and may hold clues about gravitational waves and dark matter interactions.
"""


splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0, # what is the overlap between 2 chunks. it overlaps to retain context when character splits abruptly. 
    separator=''
)

result = splitter.split_text(text)

print(result)

# for rags 10-20% chunk overlap is a good practice.