# Form Filler

## About the script

Bigots keep launching snitch-lines to encourage people to report on their<br />
neighbors for being trans or teaching American history.<br />
[Indiana](https://www.chalkbeat.org/indiana/2024/02/06/attorney-general-todd-rokita-race-gender-politics-school-curriculum-tip-line/), [Missouri](https://www.riverfronttimes.com/news/missouri-ag-removes-trans-health-care-tip-line-after-hack-39907011), and [Utah](https://apnews.com/article/transgender-bathroom-law-utah-tip-line-943112e6ff6f5768caa0cd42403957a0) have all made national news for launching,<br />
and subsequently removing, such forms. Thankfully, the internet has been<br />
more than willing to stuff these troglodytes' inboxes with [the *Bee Movie* script](https://techcrunch.com/2023/04/21/missouri-trans-snitch-form-down-after-people-spammed-it-with-the-bee-movie-script/)<br />
and other nonsense.

This project is intended to aid activists in making anyone stupid enough<br />
to publish such a form thoroughly regret their decision. Filling out<br />
forms, even with ridiculous copypasta, is time consuming, and the faster<br />
these forms come offline, the better. So the goal of this project is<br />
to automate the fill and submit process.

Unfortunately, the nature of web forms makes creating a universal autofill<br />
script difficult. This project is a work in progress. My goal is to create<br />
as much reusable code as possible and make tailoring the script to<br />
any new form that may crop up as easy as possible.

For now, the script is aimed specifically at the snitch form for<br />
[Advocates for Faith & Freedom's "Save Girls’ Sports"](https://web.archive.org/web/20250103225110/https://faith-freedom.com/savegirlssports) initiative (archive.org link,<br />
because the original form is now password protected). I didn't actually<br />
manage to finish the script before the form went away (good riddance),<br />
but I will complete it (in case they foolishly decide to republish the form).<br />
Then I will begin work on generalizing the code as much as possible.

## Acknowledgements

This script is intended to create (mostly) plausible information with<br />
which to fill the form, the idea being that submissions that aren't<br />
immediately *obviously* trolling waste more of the time of the people<br />
checking submissions. Future versions of the script will also offer<br />
options for pure shitposting.

In order to generate reasonable looking data, the script makes use of the<br />
[Mockaroo API](https://www.mockaroo.com/docs). The Mockaroo API requires<br />
an API key. Free keys are available by registering a free Mockaroo account.<br />
Or, as of this writing (2025-01-07), there is a working login on [Bugmenot](https://bugmenot.com/view/mockaroo.com).

For large blocks of text, the script also makes use of the<br />
[Folger Shakespeare API](https://www.folgerdigitaltexts.org/api), the [Bee Movie API](https://github.com/benji-lewis/Bee-Movie-API),<br />
and the [Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights).
