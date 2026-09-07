
# source ~/envs/manim/bin/activate

"""
Command to generate the slides with manim:
manim render generating_slides.py Class_Name -pqh -s --resolution 1920,1080 
"""


from turtle import left
from manim import *
from numpy import diag
my_template = TexTemplate()
my_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
my_template.add_to_preamble(r"\usepackage[normalem]{ulem}")
my_template.add_to_preamble(r"\usepackage{xcolor}")
my_template.add_to_preamble(r"\usepackage{mathtools}")
my_template.add_to_preamble(r"\definecolor{IFAE_Color}{RGB}{0,84,61}")  # esempio

IFAE_Color = ManimColor([0., 0.32941177, 0.23921569])

class BaseSlide_WithLogo(Scene):
    def setup_background(self):
        self.camera.background_color = WHITE
        
        top_bar = Rectangle(
            width=config.frame_width,
            height=0.8,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(config.frame_height / 2 - 0.2)

        bottom_bar = Rectangle(
            width=config.frame_width,
            height=1.0,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(-config.frame_height / 2)
        
        self.add(top_bar, bottom_bar)

        logo = ImageMobject("assets/IFAE_logo_SO.png").scale(0.15)
        logo.to_corner(UL, buff=0.7)
        self.add(logo)


class BaseSlide(Scene):
    def setup_background(self):
        self.camera.background_color = WHITE
        
        top_bar = Rectangle(
            width=config.frame_width,
            height=0.8,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(config.frame_height / 2 - 0.2)

        bottom_bar = Rectangle(
            width=config.frame_width,
            height=1.0,
            color=IFAE_Color,
            fill_opacity=1,
            stroke_width=0
        ).set_y(-config.frame_height / 2)
        
        self.add(top_bar, bottom_bar)

class Title(BaseSlide_WithLogo):
    def construct(self):
        self.setup_background()

        # Titolo
        title = Tex(r"\textbf{Quark mixing from muon collider neutrinos}", color=BLACK, font_size=48, tex_template=my_template,)
        
        # Presentatore e collaboratori
        presenter = Tex(r"{Presented by F. Montagno}", color=BLACK, font_size=32)
        collaborators = Tex(r"In collaboration with D. Marzocca, M. Morales-Alvarado and A. Wulzer", color=BLACK, font_size=28)

        # Raggruppa centro
        central_block = VGroup(title, presenter, collaborators).arrange(DOWN, buff=0.7)
        central_block.move_to(ORIGIN)
        self.play(LaggedStartMap(Write, central_block, lag_ratio=0.2))
        self.wait(0.3)

        event = Tex(
            r"IFAE Pizza Seminar - Jan 14, 2026",
            color=BLACK,
            font_size=24
        )
        event.to_corner(DR, buff=0.6)
        self.play(FadeIn(event))
        
        event = Tex(
            r"arXiv:2511.23288",
            color=BLACK,
            font_size=24
        )
        event.to_corner(DL, buff=0.6)
        self.play(FadeIn(event))
        
        self.wait(1)

class Outline(BaseSlide):
    def construct(self):
        self.setup_background()

        # Titolo principale
        title = Tex(
            r"\textbf{Outline}",
            color=BLACK,
            font_size=52,
            tex_template=my_template
        ).to_edge(UP, buff=1.2)
        self.add(title)

        # Colonna sinistra – già trattato
        color1 = BLACK # GRAY
        left = VGroup(
            Tex(r"\textbf{1.} What is a Muon Collider", font_size=34, color=color1, tex_template=my_template),
            Tex(r"\textbf{2.} Neutrinos from Muon Collider", font_size=34, color=color1, tex_template=my_template),
            Tex(r"\textbf{3.} CKM, PDFs and FFs", font_size=34, color=color1, tex_template=my_template),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Sottotitoli delle colonne
        left_title = Tex(
            r"\textbf{Common Ground}",
            font_size=38,
            color=IFAE_Color,  
            tex_template=my_template
        ).next_to(left, UP, buff=0.5).shift(LEFT * 1.5)
        
        
        color2 = WHITE
        # Colonna destra – da trattare
        right = VGroup(
            Tex(r"\textbf{4.} $\nu$DIS", font_size=34, color=color2, tex_template=my_template),
            Tex(r"\textbf{5.} CKM Determination", font_size=34, color=color2, tex_template=my_template),
            Tex(r"\textbf{6.} PDF Determination", font_size=34, color=color2, tex_template=my_template),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=4)

        right_title = Tex(
            r"\textbf{Key Outcomes}",
            font_size=38,
            color=IFAE_Color if color2 != WHITE else WHITE,  # puoi cambiare colore a piacere
            tex_template=my_template
        ).next_to(right, UP, buff=0.5).shift(RIGHT * 0.5)
        

        
        left_title.shift(RIGHT * -2.5)
        left_title.shift(DOWN * 0.5)
        right_title.shift(LEFT * -.5)
        right_title.shift(DOWN * 0.7)
        content = VGroup(left, right).arrange(RIGHT, buff=1.8).move_to(ORIGIN)
        content.shift(DOWN * 0.5)
        content.shift(LEFT * 0.5)

        self.add(left_title, right_title, content)

class WhatIsMuonCollider_WhereWeAre(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{What is a Muon Collider?}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = Tex(
            r"\textbf{Where we are now:}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.7)

        self.add(sub)

        # Single bullet
        bullet = Tex(
            r"• Today, particle physics is driven by the \textbf{LHC} at CERN",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.add(bullet)

        # Single bullet
        bullet = Tex(
            r"• \textbf{Higgs boson} discovery / \textbf{TeV-scale} exploration",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.add(bullet)

        # Single bullet
        bullet = Tex(
            r"• Finite lifetime → \textbf{Shutdown} in the coming decades",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.add(bullet)
        # --- Right column image ---
        diagram = ImageMobject("assets/SM.png").scale(0.2).to_edge(RIGHT, buff=0.5).to_edge(DOWN, buff=1.5)
        caption = Tex(
            r"Izaak Neutelings",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class WhatIsMuonCollider_Whatsnext(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{What is a Muon Collider?}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = Tex(
            r"\textbf{What's next?}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(UP, buff=2.)

        self.add(sub)

class MuonsProtons(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{10 TeV collisions with 10 TeV colliders}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

class WhatIsMuonCollider(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{What is a Muon Collider?}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = Tex(
            r"• A hypothetical collider based on $\mu^+\mu^-$ collisions",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.4)

        self.add(sub)
        
        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Muons are heavy →}\textbf{ negligible synchrotron radiation} \\
            &\text{→ 10 TeV energy in a compact ring}
            \end{aligned}
            """,
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)

        # --- Right column image ---
        diagram = ImageMobject("assets/mucol.png").scale(0.8).to_edge(DOWN, buff=1.)
        caption = Tex(
            r"The Muon Collider - arXiv:2504.21417",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class NeutrinosFromMuC(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Neutrinos From Muon Collider}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = MathTex(
            r"""
            \begin{aligned}
            \bullet\  &\text{Muons decay all along the collider ring, producing } 
            \nu_\mu \text{ and } \bar{\nu}_e \\
            &\text{with typical energies of \textbf{few TeV}}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.1)

        self.add(sub)
        
        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\  &\text{Strong Lorentz boost → \textbf{highly collimated neutrino beam}}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)
        
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\  &\text{Muon beam angular spread can broaden $\nu$ beam}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)    
            
        # --- Right column image ---
        diagram = ImageMobject("assets/nuDIS-setup.png").scale(1.1).to_edge(DOWN, buff=1.7)
        caption = Tex(
            r"Schematic of the $\nu$MuC experimental setup",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.8)
        self.add(caption)
        self.add(diagram)

class NeutrinosFromMuC_Luminosity(BaseSlide):
    def construct(self):
        self.setup_background()

        title = Tex(
            r"\textbf{Fixed-Target $\nu$DIS at $\nu$MuC}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        b1 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{These neutrinos enable a \textbf{parasitic fixed-target experiment in a dedicated far-forward detector}}\\
            &\text{}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.1)
        self.add(b1)

        b2 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Measure \textbf{(SI)DIS on nucleons} in the deeply-inelastic regime, (high }Q^2\text{, huge statistics)}\\
            &\text{}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(b1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(b2)

        lumi = MathTex(
            r"""
            \begin{aligned}
            \mathcal{L} = N_N \Phi_\nu = \frac{\mathcal{R}_\nu}{\mathcal{A}}\frac{\rho L \mathcal{A}}{M} = 60 \frac{\text{fb}^{-1}}{\text{year}}\frac{\rho L}{\text{g/cm}^2}\\
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).move_to(ORIGIN).shift(DOWN * -0.)
        self.add(lumi)
        
        symbols = MathTex(
            r"""
            \begin{aligned}
            \mathcal{R}_\nu &\textbf{ = neutrino rate, $10^{10}$/s}\quad
            \mathcal{A}\textbf{ = area of the target}\quad
            \rho\textbf{ = target density}\quad
            L\textbf{ = target length}\quad
            M\textbf{ = nucleon mass}
            \end{aligned}
            """,
            font_size=24,
            tex_template=my_template,
            color=IFAE_Color
        ).next_to(lumi, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(symbols)

        text = Tex(r"Assuming \textbf{5 years} of data-taking, \textbf{1 ton} cylindrical target (radius: 10 cm, L: 1 m):", 
                font_size=28,
                color=BLACK,
                tex_template=my_template
            ).next_to(symbols, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(text)
        
        integrated_lumi = MathTex(
            r"""
            \begin{aligned}
            \int\mathcal{L} = 1500\text{ ab}^{-1}\\
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(text, DOWN, buff=0.5).to_edge(LEFT, buff=5.5)
        self.add(integrated_lumi)

class NeutrinoRate(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{$\nu$ Rate at MuC}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        equation = MathTex(
            r"""
            \mathcal{R}_\nu = N f_r \frac L{C_\text{coll}} = 10^{10}/\text{s}
            """,
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(title, DOWN, buff=1).to_edge(RIGHT, buff=1)
        self.add(equation)

        text = Tex(r"Assuming \textbf{5 years} of data-taking,\\ \textbf{1 ton} cylindrical target\\($r$: 10 cm, $L_{\text{target}}$: 1 m):", 
                font_size=28,
                color=BLACK,
                tex_template=my_template
            ).next_to(equation, DOWN, buff=1.5)
        self.add(text)
        
        integrated_lumi = MathTex(
            r"""
            \begin{aligned}
            \int\mathcal{L} = 1500\text{ ab}^{-1}\\
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(text, DOWN, buff=0.5)
        self.add(integrated_lumi)

class NeutrinoEnergySpectrum(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{$\nu$ Energy Spectrum at $\nu$MuC}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = Tex(
            r"\textbf{Why is this special?}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.)

        self.add(sub)

        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{A lot of neutrinos!}
            \end{aligned}
            """,
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)


        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Energy spectrum is \textbf{accurately predicted} }\\
            &\text{unlike neutrinos from protons }
            \end{aligned}
            """,
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)
        
        spectrum = MathTex(
            r"""
            \mathcal{P}_{\nu_\mu}(E)= \frac{1}{\Gamma}\frac{d\Gamma}{dE} = \frac{1}{3\bar E}\left[5-9\left(\frac{E}{\bar E}\right)^2+4\left(\frac{E}{\bar E}\right)^3\right]
            """,
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(spectrum)

        text = MathTex(r"{\beta = (1-m_\mu^2/E_\mu^2)^{1/2} \approx 1,\quad \bar E =(1+\beta)E_\mu/2\approx E_\mu",
                font_size=28,
                color=IFAE_Color,
                tex_template=my_template
            ).next_to(spectrum, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(text)
        # --- Right column image ---
        diagram = ImageMobject("assets/nu-spectrum.png").scale(0.5).to_edge(RIGHT, buff=0.5).to_edge(DOWN, buff=1.5)
        caption = Tex(
            r"""Energy distribution of the interacting neutrinos, \\
                compared with the neutrino beam energy spectrum""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class NeutrinoEnergySpectrum2(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{$\nu$ Energy Spectrum at $\nu$MuC}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # --- Right column image ---
        diagram = ImageMobject("assets/nu-spectrum-2.png").scale(0.8).move_to(ORIGIN)
        caption = Tex(
            r"""The energy spectrum of neutrino interactions produced in
                one year, for past and planned neutrino experiments.
                The solid and dashed lines assume, respectively, a small 10 kg and a realistic 1 ton target mass""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class CKM(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{The Cabibbo-Kobayashi-Maskawa (CKM) Matrix}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Left text block
        bullets = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Quark flavours mix under \textbf{weak interactions}}\\
            \bullet\ &\text{CKM matrix encodes the strength of \textbf{charged-current transitions}}\\
            \bullet\ &\text{In the SM it is a \textbf{unitary $3\times3$ matrix}}\\
            \bullet\ &\text{Precise CKM tests probe the \textbf{consistency of the SM}}
            \end{aligned}
            """,
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.4)
        self.add(bullets)

        # CKM matrix
        matrix = MathTex(
            r"""
            |V_{\text{CKM}}| =
            \begin{pmatrix}
            0.974 & 0.225 & 0.004 \\
            0.225 & 0.973 & 0.042 \\
            0.009 & 0.041 & 0.999
            \end{pmatrix}
            """,
            font_size=32,
            color=BLACK,
            tex_template=my_template
        ).next_to(bullets, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(matrix)

        # Caption
        caption = Tex(
            r"PDG values (absolute magnitudes)",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(matrix, DOWN, buff=0.3)
        self.add(caption)
        # --- Up right column image ---
        diagram = ImageMobject("assets/quarks_SM.png").scale(0.6).to_edge(RIGHT, buff=1.).to_edge(UP, buff=2.4)
        self.add(diagram)
        # --- Right column image ---
        diagram = ImageMobject("assets/qqW.png").scale(0.8).next_to(matrix, RIGHT, buff=0.3).shift(DOWN * 0.5)
        self.add(diagram)

class PDFs(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parton Distribution Functions (PDFs)}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Single bullet
        sub = Tex(
            r"\textbf{What are PDFs?}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.)

        self.add(sub)

        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Protons (and nucleons) are } \textbf{not elementary particles}\\
            &\text{They are made of }\textbf{quarks and gluons (partons)}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)


        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{A PDF gives the probability to find a parton}\\
            &\text{carrying a fraction $x$ of the proton momentum}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)

        # Single bullet
        bullet = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{The scale $Q^2$ sets the \textbf{resolution} of the probe}\\
            &\text{higher $Q^2$ → finer resolution inside the proton}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet)        


        # --- Right column image ---
        diagram = ImageMobject("assets/PDFs.png").scale(0.6).to_edge(RIGHT, buff=0.5).to_edge(DOWN, buff=2)
        caption = Tex(
            r"""PDF4LHC21 for different channels at $Q^2 = 400 \text{ GeV}^2$""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class FFs(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Fragmentation Functions (FFs)}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Subtitle
        sub = Tex(
            r"\textbf{Why FFs? (SIDIS)}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.)
        self.add(sub)

        # Bullet 1
        bullet1 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{In \textbf{SIDIS} we measure a \textbf{tagged hadron} in the final state}\\
            &\text{(e.g. }K^\pm,\ D^{*\pm},\ B\text{-hadrons)}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet1)

        # Bullet 2
        bullet2 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{FFs give the probability that a \textbf{parton} produces}\\
            &\text{a given hadron carrying a fraction $z$ of the parton energy}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet2)

        # Bullet 3
        bullet3 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{The scale $Q^2$ controls the \textbf{evolution} of FFs (as for PDFs)}\\
            &\text{FFs are essential for \textbf{flavour tagging} in $\nu$SIDIS}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet2, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet3)

        # --- Right column image ---
        diagram = ImageMobject("assets/FFs.png").scale(0.7).to_edge(RIGHT, buff=0.18).to_edge(DOWN, buff=2.2)
        caption = Tex(
            r"""Fragmentation functions of $D^{*+}$ meson for\\ different partons,
                with 68\% CL uncertainty bands""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)

class DIS(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Deep Inelastic Scattering (DIS)}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)
        diagram = ImageMobject("assets/DIS.png").scale(0.5).to_edge(RIGHT, buff=0.3).to_edge(DOWN, buff=1.6)
        caption = Tex(
            r"""Number of events distribution in $x–Q^2$ bins""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(caption)
        self.add(diagram)
        # Subtitle
        sub = Tex(
            r"\textbf{Neutrino--nucleon scattering}",
            font_size=40,
            tex_template=my_template,
            color=BLACK
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=1.8)
        self.add(sub)

        process = MathTex(
            r"""
            \begin{aligned}
            \textbf{Charged Current (CC):}\quad
            &\nu_\mu + N \;\longrightarrow\; \mu^- + X\\
            &\bar{\nu}_e + N \;\longrightarrow\; e^+ + X\\[0.3cm]
            \textbf{Neutral Current (NC):}\quad
            &\nu + N \;\longrightarrow\; \nu + X
            \end{aligned}
            """,
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(sub, DOWN, buff=0.6).to_edge(LEFT, buff=1)

        self.add(process)

        # DIS formula (schematic)
        # formula = MathTex(
        #     r"""
        #     \frac{d^2\sigma}{dx\,dQ^2}
        #     \;\sim\;
        #     \sum_{q,q'}
        #     \underbrace{|V_{qq'}|^2}_{\text{CKM}}
        #     \;
        #     \underbrace{f_q(x,Q^2)}_{\text{PDF}}
        #     \;
        #     \times\;
        #     \text{kin}(x,Q^2)
        #     """,
        #     font_size=32,
        #     color=BLACK,
        #     tex_template=my_template
        # ).next_to(process, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        # self.add(formula)
        formula = MathTex(
            r"""
            \frac{d^2\sigma}{dx\,dQ^2}
            \;\sim\;
            \sum_{q,q'}
            |V_{qq'}|^2
            \;
            {f_q(x,Q^2)
            \;
            \times\;
            \text{kin}(x,Q^2)
            \times\;
            \textcolor{IFAE_Color}{\underbrace{F_{h/q'}(z,Q^2)}_{\text{FF (SIDIS only)}}}

            """,
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).next_to(process, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(formula)
        # Interpretation bullets
        bullets = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{\textcolor{black}{DIS directly probes \textbf{quark flavour and momentum}}}\\
            \bullet\ &\text{\textcolor{black}{CKM elements control the \textbf{weak transition}}}\\
            \bullet\ &\text{\textcolor{black}{PDFs encode the \textbf{nucleon structure}}}
            \end{aligned}
            """,
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).to_edge(DOWN, buff=0.8).to_edge(LEFT, buff=1)
        self.add(bullets)
            # r"""
            # \begin{aligned}
            # \bullet\ &\text{DIS directly probes \textbf{quark flavour and momentum}}\\
            # \bullet\ &\text{CKM elements control the \textbf{weak transition}}\\
            # \bullet\ &\text{PDFs encode the \textbf{nucleon structure}}
            # \end{aligned}
            # """,
        # --- Right column image ---

        

class Events(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Number of DIS Events at $\nu$MuC}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        diagram = ImageMobject("assets/events.png").scale(1).move_to(ORIGIN)
        caption = Tex(
            r"""The DIS and SIDIS processes with the corresponding  \\
            total number of expected events with a tungsten nucleon (denoted as W)""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(diagram)
        self.add(caption)

class Observables(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Observables}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        diagram = ImageMobject("assets/observables.png").scale(0.8).move_to(ORIGIN)
        caption = Tex(
            r"""The observables employed in the fit""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(diagram)
        self.add(caption)

class ParametricUncertainties(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Parametric Uncertainties}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # # Subtitle
        # sub = Tex(
        #     r"\textbf{Treatment in the fit}",
        #     font_size=40,
        #     tex_template=my_template,
        #     color=BLACK
        # ).to_edge(LEFT, buff=1).to_edge(UP, buff=2.)
        # self.add(sub)

        # Bullet 1
        bullet1 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Parameters of interest: \textbf{CKM elements} and } \sin\theta_W\\
            &\text{Observables depend on \textbf{PDFs} and \textbf{Fragmentation Functions}}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(title, DOWN, buff=1.).to_edge(LEFT, buff=1)
        self.add(bullet1)

        # Bullet 2
        bullet2 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{PDF and FF uncertainties are included via \textbf{nuisance parameters}}\\
            &\text{ Hessian representations of the PDFs and of the FFs }\rightarrow\\
            &f_\alpha(\xi,Q^2;\nu) = f_\alpha^{(0)}(\xi,Q^2) + \sum_{k=1}^{N} \nu_k \left[f_\alpha^{(k)}(\xi,Q^2)-f_\alpha^{(0)}(\xi,Q^2)\right]
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet2)

        # Bullet 4
        bullet4 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Predictions are \textbf{linearised} in nuisance parameters}\\
            &\text{→ likelihood is quadratic and can be \textbf{profiled analytically}}
            \end{aligned}
            """,
            font_size=28,
            tex_template=my_template,
            color=BLACK
        ).next_to(bullet2, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.add(bullet4)

class CKM_Results(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{CKM matrix elements determination}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)


        diagram = ImageMobject("assets/CKM-Determination.png").scale(1).move_to(ORIGIN).shift(UP * 0.2)
        caption = Tex(
            r"""Relative global precision, in \%, on the absolute values \\
                of CKM elements and on $\sin\theta_W$ from the PDG and after \\
                adding measurements at the 10 TeV $\nu$MuC in the baseline fit configuration""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(diagram, DOWN, buff=0.2)
        self.add(diagram)
        self.add(caption)

class CKM_Results_Plot(BaseSlide):
    def construct(self):
        self.setup_background()

        # --- Title (optional) ---
        title = Tex(
            r"\textbf{CKM matrix elements determination}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # --- Load plots ---
        # Replace with your actual paths
        p1 = ImageMobject("assets/ckm-1.png")
        p2 = ImageMobject("assets/ckm-2.png")
        p3 = ImageMobject("assets/ckm-3.png")
        # p4 = ImageMobject("assets/ckm-4.png")

        plots = Group(p1, p2, p3)  # , p4)

        # Make them all the same size (match the smallest one)
        plots.arrange_in_grid(rows=1, cols=3, buff=0.35)
        plots.set(height=3.5)  # overall grid height (tune)
        # Alternatively control width instead:
        # plots.set(width=12.5)

        plots.next_to(title, DOWN, buff=1)
        plots.move_to(plots.get_center())  # keeps it centered

        self.add(plots)

        caption = Tex(
            r"""68\% CL ellipses for CKM pairs, showing the PDG prior (red) \\and the baseline fit (blue)""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(plots, DOWN, buff=0.3)
        self.add(caption)

class PDF_Plot(BaseSlide):
    def construct(self):
        self.setup_background()

        # --- Title (optional) ---
        title = Tex(
            r"\textbf{PDF determination}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # --- Load plots ---
        # Replace with your actual paths
        p1 = ImageMobject("assets/pdf-1.png")
        p2 = ImageMobject("assets/pdf-2.png")
        p3 = ImageMobject("assets/pdf-3.png")

        plots = Group(p1, p2, p3)  # , p4)

        # Make them all the same size (match the smallest one)
        plots.arrange_in_grid(rows=1, cols=3, buff=0.35)
        plots.set(height=3.2)  # overall grid height (tune)
        # Alternatively control width instead:
        # plots.set(width=12.5)

        plots.next_to(title, DOWN, buff=1)
        plots.move_to(plots.get_center())  # keeps it centered

        self.add(plots)

        caption = Tex(
            r"""PDF uncertainties expected at the $\nu$MuC experiment, compared with current uncertainties from PDF4LHC21""",
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(plots, DOWN, buff=0.3)
        self.add(caption)

class Conclusions(BaseSlide):
    def construct(self):
        self.setup_background()

        # Title
        title = Tex(
            r"\textbf{Conclusions}",
            color=BLACK,
            font_size=48,
            tex_template=my_template
        ).to_edge(UP, buff=1)
        self.add(title)

        # Bullets (left column)
        b1 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{A \textbf{parasitic neutrino experiment} at a muon collider ($\nu$MuC)}\\
            &\text{enables a \textbf{radical improvement} in CKM determination}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).to_edge(LEFT, buff=1).to_edge(UP, buff=2)
        self.add(b1)

        b2 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Novel and \textbf{independent} methodology from low-energy measurements}\\
            &\text{based on a global analysis of \textbf{DIS and SIDIS}}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(b1, DOWN, buff=0.6).to_edge(LEFT, buff=1)
        self.add(b2)

        b4 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{A strong improvement in \textbf{PDF determination} emerges as a byproduct}\\
            &\text{}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(b2, DOWN, buff=0.6).to_edge(LEFT, buff=1)
        self.add(b4)

        b5 = MathTex(
            r"""
            \begin{aligned}
            \bullet\ &\text{Excellent performance already at \textbf{3 TeV}, with best reach at \textbf{10 TeV}}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(b4, DOWN, buff=0.6).to_edge(LEFT, buff=1)
        self.add(b5)
        
        # Bullets (right column)
        
        #subtitle
        sub = Tex(
            r"\textbf{\textcolor{IFAE_Color}{Future directions}}",
            font_size=32,
            tex_template=my_template,
            color=BLACK
        ).to_edge(RIGHT, buff=1.5).to_edge(UP, buff=1.8)
        #self.add(sub)
        
        bb1 = MathTex(
            r"""
            \begin{aligned}
            \textcolor{IFAE_Color}{\bullet}\ &\text{\textcolor{IFAE_Color}{Assessment of QCD uncertainties}}\\
            &\text{}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(sub, DOWN, buff=0.5).to_edge(LEFT, buff=10)
        #self.add(bb1)
        
        bb2 = MathTex(
            r"""
            \begin{aligned}
            \textcolor{IFAE_Color}{\bullet}\ &\text{\textcolor{IFAE_Color}{PDF Fit from scratch}}\\
            &\text{}
            \end{aligned}
            """,
            font_size=24,
            color=BLACK,
            tex_template=my_template
        ).next_to(bb1, DOWN, buff=0.5).to_edge(LEFT, buff=10)
        #self.add(bb2)
        # Closing line / takeaway (bottom)
        takeaway = Tex(
            r"\textbf{Muon-collider neutrinos add a powerful new precision program to the MuC physics case.}",
            font_size=28,
            color=BLACK,
            tex_template=my_template
        ).to_edge(DOWN, buff=1)
        #self.add(takeaway)


###############################