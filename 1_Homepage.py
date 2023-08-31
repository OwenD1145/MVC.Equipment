import streamlit as st
import base64

st.set_page_config(
  page_title="MVC Tools - Homepage",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header("MVC Tools of the Trade")
st.markdown("##")

 @gather_metrics("caption")
    def caption(
        self,
        body: SupportsStr,
        unsafe_allow_html: bool = False,
        *,  # keyword-only arguments:
        help: Optional[str] = None,
    ) -> "DeltaGenerator":
        """Display text in small font.

        This should be used for captions, asides, footnotes, sidenotes, and
        other explanatory text.

        Parameters
        ----------
        body : str
            The text to display as Github-flavored Markdown. Syntax
            information can be found at: https://github.github.com/gfm.

            This also supports:

            * Emoji shortcodes, such as ``:+1:``  and ``:sunglasses:``.
              For a list of all supported codes,
              see https://share.streamlit.io/streamlit/emoji-shortcodes.

            * LaTeX expressions, by wrapping them in "$" or "$$" (the "$$"
              must be on their own lines). Supported LaTeX functions are listed
              at https://katex.org/docs/supported.html.

            * Colored text, using the syntax ``:color[text to be colored]``,
              where ``color`` needs to be replaced with any of the following
              supported colors: blue, green, orange, red, violet, gray/grey, rainbow.

        unsafe_allow_html : bool
            By default, any HTML tags found in strings will be escaped and
            therefore treated as pure text. This behavior may be turned off by
            setting this argument to True.

            That said, *we strongly advise against it*. It is hard to write secure
            HTML, so by using this argument you may be compromising your users'
            security. For more information, see:

            https://github.com/streamlit/streamlit/issues/152

        help : str
            An optional tooltip that gets displayed next to the caption.

        Examples
        --------
        >>> import streamlit as st
        >>>
        >>> st.caption('This is a string that explains something above.')
        >>> st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

        """
        caption_proto = MarkdownProto()
        caption_proto.body = clean_text(body)
        caption_proto.allow_html = unsafe_allow_html
        caption_proto.is_caption = True
        caption_proto.element_type = MarkdownProto.Type.CAPTION
        if help:
            caption_proto.help = help
        return self.dg._enqueue("markdown", caption_proto)

hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     # Embedding PDF in HTML
#     global pdf_display
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)
# displayPDF("2019_dbc.pdf")
st.markdown(hide_st_style, unsafe_allow_html=True)
# st.markdown(pdf_display, unsafe_allow_html=True)
