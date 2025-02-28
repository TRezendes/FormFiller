# Form Filler

## This Version Fills the Form at <https://enddei.ed.gov/>

## About the script

Bigots keep launching snitch-lines to encourage people to report on their<br />
neighbors for being trans or teaching American history. [Indiana][Indiana], [Missouri][Missouri],<br />
and [Utah][Utah] have all made national news for launching, and subsequently removing,<br />
such forms. Thankfully, the internet has been more than willing to stuff these<br />
troglodytes' inboxes with [the *Bee Movie* script][TechCrunchBeeMovie] and other nonsense.

This project is intended to aid activists in making anyone stupid enough to publish<br />
such a form thoroughly regret their decision. Filling out forms, even with<br />
ridiculous copypasta, is time consuming, and the faster these forms come offline,<br />
the better. So the goal of this project is to automate the fill and submit process.

Unfortunately, the nature of web forms makes creating a universal autofill script<br />
difficult. This project is a work in progress. My goal is to create as much reusable<br />
code as possible and  make tailoring the script to any new form that may crop up<br />
as easy as possible.

For now, the script is aimed specifically at the disgusting [Do No Harm][DNHwiki]<br />
organization's ["Submit Your Concern" form][DNHform].

## Using the Script

The script is setup to use Selenium browser automation in Firefox. If you want to<br />
use a different browser, you will need to edit the script to do so.<br />
In future versions, I would like to use TOR, but some quick searching suggests<br />
that using Selenium with TOR can be tricky, and for now, I just want to get this<br />
out in the world.

### Command Line Usage

```
usage: filler.py [-h] [-n NUM_SUBS] [-c {b,s,u}] [-f]

options:
  -h, --help            show this help message and exit
  -n, --num-subs NUM_SUBS
                        The number of times to fill and submit the form.
                        type: int
                        default: 1
  -c, --content {b,s,u}

                        Select which content with which to fill the form.
                        b, s, & u use faker to fill plausible data in the short text fields (name, email address, phone number, etc.).
                        For the 500 character textarea field ('Incident Details') and the optional uploaded files
                        b uses the Bee Movie transcript,
                        s uses text from a random Shakespeare play, and
                        u uses the text of the Universal Declaration of Human Rights.
                        s & b both fall back to u if their respective API call fails.
                        g [NOT IMPLEMENTED YET] fills all text fields and the files with randomly generated gibberish.
                        type: str
                        default: s

  -f, --include-files   [NOT IMPLEMENTED YET] Set this flag to generate and upload 3 5MB files (the form's maximum) with the form submission.

```

## Acknowledgements

This script is intended to create (mostly) plausible information with which to<br />
fill the form, the idea being that submissions that aren't immediately *obviously*<br />
trolling waste more of the time of the people checking submissions.<br />
Future versions of the script will also offer options for pure shitposting.

The script uses the [faker][faker] package and the [faker_education][fakerEd]<br />
provider to generate reasonable looking data.

For large blocks of text, the script also makes use of the [Folger Shakespeare API][shakespeare],<br />
the [Bee Movie API][beeMovieAPI] and the [Universal Declaration of Human Rights][udhr].


[Indiana]: <https://www.chalkbeat.org/indiana/2024/02/06/attorney-general-todd-rokita-race-gender-politics-school-curriculum-tip-line/> "Indiana schools weren’t warned of AG Todd Rokita’s new curriculum tip line - Chalkbeat"
[Missouri]: <https://www.riverfronttimes.com/news/missouri-ag-removes-trans-health-care-tip-line-after-hack-39907011> "Missouri AG Removes Trans Health Care Tip Line After 'Hack'"
[Utah]: <https://apnews.com/article/transgender-bathroom-law-utah-tip-line-943112e6ff6f5768caa0cd42403957a0> "Transgender activists flood Utah tip line with hoax reports to block bathroom law enforcement | AP News"
[TechCrunchBeeMovie]: <https://techcrunch.com/2023/04/21/missouri-trans-snitch-form-down-after-people-spammed-it-with-the-bee-movie-script/> "Missouri trans 'snitch form' down after people spammed it with the 'Bee Movie' script | TechCrunch"
[DNHwiki]: <https://en.wikipedia.org/wiki/Do_No_Harm_(organization)> "'Do No Harm (organization)' on Wikipedia"
[DNHform]: <https://donoharmmedicine.org/share-your-concern/> "Submit Your Concern - Do Not Harm"
[faker]: <https://github.com/joke2k/faker> "joke2k/faker: Faker is a Python package that generates fake data for you."
[fakerEd]: <https://github.com/matthttam/faker_education> "matthttam/faker_education: Faker provider with education related data"
[shakespeare]: <https://www.folgerdigitaltexts.org/api> "The Folger Shakespeare API Tools"
[beeMovieAPI]: <https://github.com/benji-lewis/Bee-Movie-API> "benji-lewis/Bee-Movie-API"
[udhr]: <https://www.un.org/en/about-us/universal-declaration-of-human-rights> "Universal Declaration of Human Rights | United Nations"

---

[![License: OQL](https://badgers.space/badge/License/OQL/pink)](https://oql.avris.it/license/v1.2)
