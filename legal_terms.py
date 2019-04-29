import numpy as np

legal_terms = ['Abandonment', 'Abolish', 'Abridge', 'Accessory', 'Accomplice', 'Accord', 'Accused', 'Acquisitions', 'Acquittal', 'Action', 'Adjournment', 
'Administer', 'Adoption', 'Affect','Affidavit', 'Agency', 'Agent', 'Agreement', 'Alias', 'Alibi', 'Alienation', 'Alimony', 'Amend', 'Amendment', 'Annulment', 
'Appeal', 'Appoint', 'Appraisal', 'Arraignment', 'Arson', 'Aspect','Assault', 'Assembly', 'Assistance', 'Attachment', 'Attitude', 'Authorize', 'Autopsy', 'Bail',
'Bankrupt', 'Basis', 'Battery', 'Before the bar', 'Belief', 'Bench', 'Bill', 'Blackmail', 'Bond','Branch', 'Breach', 'Bribery', 'Brief', 'Burden', 'Burglary', 
'Business law', 'Case number', 'Challenge', 'Civil', 'Civil action', 'Claim', 'Code', 'Codicil', 'Coercion', 'Collusion','Commercial', 'Commission', 'Committal', 
'Common-law', 'Community property', 'Compensation', 'Complainant', 'Complication', 'Conduct', 'Confession', 'Conglomerate', 'Consent', 'Consideration', 
'Conspiracy', 'Constitution', 'Contempt', 'Contract', 'Copyright', 'Coroner', 'Corporate', 'Corporation', 'Costly', 'Counsel', 'Counterfeit', 'Court', 'Credit', 
'Crime', 'Criminal,Damages', 'Deal', 'Dealings', 'Debt', 'Decision', 'Decree', 'Deed', 'Defendant', 'Defense', 'Deliberate', 'Democratic', 'Denial', 'Deposition', 
'Desertion', 'Determination','Disobedience', 'Disregard', 'Divorce', 'Document', 'Documentation', 'Draft', 'Due process','Easement', 'Edict', 'Educate', 'Effect', 
'Embezzle', 'Eminent domain', 'Emphasis', 'Enable','Encumber', 'Enforce', 'Entail', 'Equality', 'Escrow', 'Estate', 'Ethics', 'Eviction', 'Evidence', 
'Examination', 'Excessive', 'Executor', 'Expert', 'Extort', 'Extradition', 'Extreme','Failure', 'Fairness', 'Family', 'Federal', 'Fee', 'Felony', 'Fines', 
'Forgery', 'Fraud', 'Freedom', 'Fundamental', 'Funds', 'Garnishment', 'Govern', 'Guarantee', 'Guaranty', 'Guardian', 'Guilty','Habeas corpus', 'Harmful', 'Heir', 
'High-ranking', 'Hijack', 'Homicide', 'Honor','Impartial', 'Imprison', 'Incompetent', 'Indictment', 'Influence', 'Inform', 'Inheritance','Initiative', 'Injunction',
'Injury', 'Inquest','Interests', 'Interference', 'Interpretation', 'Interstate', 'Issue','Jeopardy', 'John Doe', 'Joint tenancy', 'Judge', 'Judgment', 'Judicial',
'Jurisprudence', 'Jury', 'Justice', 'Juvenile', 'Kidnapping', 'Kin', 'Larceny', 'Law', 'Lawfully', 'Lawsuit', 'Lease', 'Legacy', 'Legal', 'Legal assistance', 
'Legislation','Liability', 'Libel', 'Liberty', 'License', 'Lien', 'Limits', 'Litigation', 'Loan', 'Lynch', 'Majority', 'Malice', 'Malpractice', 'Manslaughter', 
'Mayhem', 'Merger', 'Minority','Misdemeanor', 'Moratorium', 'Mortgage', 'Murder', 'Natural law', 'Negligent', 'Negotiable', 'Notation', 'Notice', 'Nuisance', 
'Oath', 'Obedience', 'Obey', 'Obligation', 'Offense', 'Official', 'Opinion', 'Organize', 'Out-dated', 'Overturn', 'Ownership', 'Paralegal', 'Partnership', 'Patent'
,'Penalize', 'Penalty', 'People', 'Perjury', 'Petition', 'Power','Power of attorney', 'Practice', 'Pre-law', 'Precedent', 'Press', 'Previous', 'Principle', 'Prior',
'Prison', 'Private', 'Probable cause', 'Probate', 'Professional', 'Prohibit','Proof', 'Property', 'Prosecute', 'Prosecutor', 'Protection', 'Provision, Public', 
'Punishment', 'Qualification', 'Quality', 'Quantify', 'Quantity', 'Question', 'Quirk', 'Quorum','Rate', 'Reasoning', 'Receiver', 'Redress', 'Reduction', 
'Referendum', 'Refute', 'Regulate', 'Rejection', 'Religion', 'Repeal', 'Reputation', 'Resist', 'Responsibility', 'Restriction','Reverse', 'Rights', 'Robbery',
'Rules', 'Rulings', 'Sabotage', 'Safeguard', 'Sanction', 'Sealed record', 'Security', 'Selection', 'Seriousness', 'Services', 'Skillful', 'Slander','Smuggling',
'Special-interest', 'Standard', 'Statute', 'Statute of limitation', 'Subpoena', 'Suit', 'Summons', 'System', 'Tenant', 'Testament', 'Testimony', 'Title', 'Tort', 
'Trademark','Tradition', 'Transfer', 'Treason', 'Treatment', 'Treaty', 'Trespass', 'Trial', 'Trial by jury', 'Trust', 'Trustee', 'Unalienable', 'Unauthorized',
'Unclaimed', 'Unconstitutional','Unintentional', 'Unjust', 'Unlawful', 'Uphold','Usury' , 'Vagrancy', 'Vandalism', 'Verdict', 'Veto', 'Victim', 'Victimize', 
'Violate', 'Violation', 'Volume', 'Ward', 'Well-developed','Will', 'Wisdom', 'Witness', 'Writ', 'Wrong', 'Youth', 'Zeal']

legal_terms = [w.lower() for w in legal_terms]

import pickle

with open('LegalTerms', 'wb') as fp:
    pickle.dump(legal_terms, fp)

with open ('LegalTerms', 'rb') as fp:
    itemlist = pickle.load(fp)

print(itemlist)