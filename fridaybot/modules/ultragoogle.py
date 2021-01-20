        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
**Possible Related Search**: <a href="{prs_url}">{prs_text}</a>
More Info: Open this <a href="{the_location}">Link</a> in {ms} seconds""".format(
        OUTPUT_STR = """/protecc {prs_text}""".format(
            **locals()
        )
    await event.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)
