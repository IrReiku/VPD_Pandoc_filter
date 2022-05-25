import sys
import panflute as pf

headers = []


def existingHeading(elem, doc):
    if isinstance(elem, pf.Header):
        headingName = pf.stringify(elem)
        if headingName in headers:
            sys.stderr.write("В документе несколько заголовков с именем \"" + headingName + "\"\n")
        else:
            headers.append(headingName)


def capitaliseHeading(elem, doc):
    if isinstance(elem, pf.Header):
        if elem.level > 2:
            return pf.Header(pf.Str(pf.stringify(elem).upper()), level=elem.level)


def makeBold(doc):
    doc.replace_keyword('BOLD', pf.Strong(pf.Str('BOLD')))


if __name__ == '__main__':
    pf.run_filters([existingHeading, capitaliseHeading], prepare=makeBold)
