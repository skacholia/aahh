import openai
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Athens Area Habitat for Humanity 🏠", page_icon=":house:", layout="wide")


st.title("Your AI-powered Marketing Tool")
st.subheader("A custom app built by **Athens AI**")

openai.api_key = st.secrets["oai-key"]


sections = st.selectbox(
    'What blog section would you like to write?',
    ('Building the Community', 'The Giving Spirit', 'Volunteer Spotlight', 'Local Partners',
     'What We\'re Up To', 'Homeowner Tips', 'Other'))
# Get API key

prompt_giving = "This past year, the need for cost-manageable housing was greater than we’ve ever seen it. So we set our sights high for our annual fund drive. And local Habitat supporters came through!" \
                "We raised a record $54,632 during our annual campaign, exceeding our goal. These donations will be combined with Foundation Donor contributions and other yearlong donations, " \
                "federal and state and private foundation grants, return revenue from our no-interest mortgage holders and income-adjusted lease holders, and funds raised " \
                "through our ReStores to make new work possible in the coming years." \
                "A special thanks goes out to all our new and longstanding Foundation Donors who provide Athens Area Habitat with a " \
                "predictable funding base for our General Fund by committing to a regular automatic donation at the amount and interval of their choosing. " \
                "Your reliable support allows us to plan ahead for exciting and innovative projects to build our community. If you’re not yet a donor, " \
                "but you’d like to be, visit our donation page here: https://www.athenshabitat.com/donate"

prompt_volunteer = "Paul Anderson has volunteered more than 1000 hours with Athens Area Habitat. And he’s only been volunteering for about a year!" \
                "\nIt started in 2018 when he volunteered “sweat equity” on the future home of his stepdaughter, " \
                "Roslyn Brooks. All Habitat homeowner partners participate in the building of their home, or volunteer " \
                "on other homes, but friends and family can donate their hours to the homeowner as Paul so generously chose to do. " \
                "And he plans to continue donating his volunteer time to new families working toward their first home."

prompt_partner = "You need food for fuel if you’re going to get anything done, especially building a house!" \
                "Our solution: Athens Area Habitat’s “Build an Appetite” program, through which local restaurants and caterers " \
                "donate regular meals for our hungry crew and volunteers on weekends and special build days. And we can assure you, " \
                "it’s always the favorite part of the build day! [Partner 1], [Partner 2], and [Partner 3] " \
                "became the first members of the [Program], and [Partner 4] has since joined the roster." \
                "We’re so thankful to [Our partners] for keeping such an awesome program going, " \
                "and can’t wait to see how it continues to grow. So don’t forget to support your local businesses who are giving back!" \
                "(And if you’d like to get involved with the AAHFH Build an Appetite program, please contact our outreach director, " \
                 "Hannah Mitchell, at outreach@athenshabitat.com.)"

prompt_home = "Autumn is beautiful, but like all seasons it has its share of pitfalls. Here are three smart tips for homeowners around Athens: " \
                "**Before you stow your mower**: Did you know that gasoline has a shelf life? Yup, once it’s dispensed, if it’s left sitting too " \
                "long some of the hydrocarbons will evaporate, others will oxygenate, and a substance called gum begins " \
                "to form which is pretty much what it sounds like and you don’t want it in your engine. So either drain your " \
                "tank and lines before storing your mower or add some fuel stabilizer to the tank so it can overwinter safely." \
                "**One step for beautiful moss**: If you have hard soil in a shady area where grass won’t grow, one option is to let the moss take over. " \
                "It’s pretty, requires no fertilizer, and is resistant to pests. But if you go this route, one step you need to take is to keep the leaves " \
                "off in autumn. You can give it a pass with a bagging mower, or spend an afternoon getting some exercise by breaking out the rake."\
                "**Get your flue shot**: Don’t wait until it’s time to build a fire in your fireplace or wood stove — have your flue inspected now. " \
                "There’s no other way to know if you have a dangerous buildup of creosote in your flue (which can ignite at just over 450 degrees) or " \
                "blockages from bird nests or debris. More than 25,000 chimney fires are set off every year in the US, causing over $100 million in property " \
                "damage and around 500 deaths. So be safe and have your flue checked, and cleaned if necessary, before you light that first fire of the season."


# Create a function that uses GPT to write a blog post
def generic_completion(prompt, max_tokens):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt= prompt,
        max_tokens= max_tokens,
        n=1,
        stop=None,
        temperature=0.85,
    )

    message = completions.choices[0].text
    return message.strip()

def tweet(output):
    return generic_completion(
        "Generate a tweet for Athens Habitat for Humanity summarizing the following text."
        "Make it engaging, and use a friendly, Southern tone:" + output, 30)

if sections == 'Building the Community':
    event = st.text_area("Is there an event? If so, what are the details?")
    updates = st.text_area("Any other updates?")
    facts = st.text_area("Any facts, studies, or details to mention?")
    if st.button(label="Generate Post"):
        try:
            output = generic_completion(
                "Generate a detailed, lengthy blog post for Athens Area Habitat for Humanity about " + updates +
                ". Mention the event: " + event + ". Also mention these facts: " + facts +
                "Use a friendly Southern tone." +
                "\nPost: ", 1300)
            st.write("```")
            st.write(output)
            st.write("```")
            components.html(
                f"""
                                            <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-text="{tweet(output)}" data-url="https://www.athenshabitat.com/blog/"
                                            data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                                        """,
                height=45,
            )
        except:
            st.write("An error occurred while processing your request.")

elif sections == 'The Giving Spirit':
    donations = st.text_input("We received this amount in donations:")
    donor = st.text_input("From:")
    details = st.text_area("Some details include:")

    if st.button(label="Generate Post"):
        try:
            output = generic_completion(
                "Generate a blog post for Athens Area Habitat for Humanity about receiving " + donations + " from " +
                donor + ". Here are some more details: " + details +
                "Use a friendly Southern tone and base the post on the following example: " + prompt_giving +
                "\nNew: ", 1000)
            st.write("```")
            st.text_area(output)
            st.write("```")
            components.html(
                f"""
                                            <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-text="{tweet(output)}" data-url="https://www.athenshabitat.com/blog/"
                                            data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                                        """,
                height=45,
            )
        except:
            st.write("An error occurred while processing your request.")

elif sections == 'Volunteer Spotlight':
    volunteer = st.text_input("Who should we thank?")
    details = st.text_input("What should we know about them?")
    quotes = st.text_area("Any quotes to include?")

    if st.button(label="Generate Post"):
        try:
            output = generic_completion("Generate a Volunteer Spotlight blog post for Athens Area Habitat for Humanity about  " + volunteer + ". " \
                                        "Here is some information about them: " + details + ". Use a friendly Southern tone." +  "Include these quotes: " + quotes +
                                        "\nBase the post on the following example: " + prompt_volunteer +
                                        "\nNew: ", 1000)
            st.write("```")
            st.write(output)
            st.write("```")
            components.html(
                f"""
                                <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-text="{tweet(output)}" data-url="https://www.athenshabitat.com/blog/"
                                data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                            """,
                height=45,
            )

        except:
            st.write("An error occurred while processing your request.")

elif sections == 'Local Partners':
    partners = st.text_input("Which partners to thank?")
    context = st.text_area("What did they do?")
    other = st.text_input("Anything else to mention?")
    if st.button(label="Generate Post"):
        try:
            output = generic_completion("Generate a detailed and lengthy blog post for Athens Area Habitat for Humanity thanking partners " + partners + ". " \
                                        "They helped by: " + context + " " + "Also, " + other + "Use a grateful Southern tone."
                                        "Base the post on the following example: " + prompt_partner +
                                        "\nNew: ", 1000)
            st.write("```")
            st.text_area(output)
            st.write("```")
            components.html(
                f"""
                                            <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-text="{tweet(output)}" data-url="https://www.athenshabitat.com/blog/"
                                            data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                                        """,
                height=45,
            )
        except:
            st.write("An error occurred while processing your request.")

elif sections == 'What We\'re Up To':
    updates = st.text_area("What are your updates?")
    details = st.text_area("What are some details to include?")
    if st.button(label="Generate Post"):
        try:
            output = generic_completion("Generate a three paragraph, detailed blog post for Athens Area Habitat for Humanity."
                                        "Use a friendly Southern tone. Keep in mind that Athens-Clarke County has among the highest poverty rates and "
                                        "lowest home ownership rates in the United States, and our mission is to build, renovate and repair "
                                        "decent, affordable houses for everyone."
                                        "Base the post on the following updates: " + updates +
                                        ". And these details: " + details, 1300)
            st.write("```")
            st.write(output)
            st.write("```")
            components.html(
                f"""
                                            <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-text="{tweet(output)}" data-url="https://www.athenshabitat.com/blog/"
                                            data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                                        """,
                height=45,
            )
        except:
            st.write("An error occurred while processing your request.")

elif sections == 'Homeowner Tips':
    season = st.selectbox(
    'What season is it?',
        ('Spring', 'Summer', 'Fall', 'Winter'))
    if st.button(label="Generate Post"):
        try:
            st.write("```")

            output = generic_completion("Generate three, detailed homeowner tips. Each tip should be 4-5 sentences, and be clever. "
                                        "Separate each tip with a new line. Make it specific to Athens, Georgia. The season is " + season + ". " \
                                        "Example: " +
                                        prompt_home + "\n"
                                        "New: ", 800)
            st.write(output)
            st.write("```")
        except:
            st.write("An error occurred while processing your request.")

else:
    prompt = st.text_area("What should we write about?")
    if st.button(label="Generate Post"):
        try:
            st.write("```")

            output = generic_completion("Generate a detailed, lengthy blog post for Athens Area Habitat for Humanity. Use "
                                        "a friendly Southern tone. The topic is " + prompt)
            st.write(output)
            st.write("```")
            tweet = generic_completion(
                "Generate a tweet for Athens Habitat for Humanity summarizing the following text."
                "Make it engaging, and use a friendly, Southern tone:" + output)
            components.html(
                f"""
                                              <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large" data-text="{tweet} data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                                           """, height=45)
        except:
            st.write("An error occurred while processing your request.")

