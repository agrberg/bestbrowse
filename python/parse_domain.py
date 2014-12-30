from urlparse import urlparse

def parse_domain(url, levels=2):
    """
    Given a URL or hostname, returns the domain to the given level (level 1 is the top-level domain).
    Uses a list of active top-level domains to ensure long TLD's such as ".co.uk" are correctly treated as a single TLD.
    If the domain has an unrecognizable TLD, assumes it is one level.
    """
    if levels < 1 or not url:
        return None
        
    # Parse the hostname from the url
    parsed = urlparse(url)
    hostname = getattr(parsed,'netloc',url)
    
    partial_domains = []
    partial_domain = ""
    for section in reversed(hostname.split(".")):
        partial_domain = "." + section + partial_domain
        partial_domains.append(partial_domain)
        
    # Find the longest matching TLD, recording its index
    tld_idx = 0
    for idx, item in enumerate(partial_domains):
        if item in tlds:
            tld_idx = idx
        
    # Add the desired number of levels to the tld index,
    # counting the TLD itself as the first level
    try:
        domain = partial_domains[tld_idx + levels - 1]
    except IndexError:
        domain = partial_domains[-1]
    
    # Remove the initial dot
    return domain[1:]
        
tlds = set((
    '.2000.hu',
    '.ab.ca',
    '.ab.se',
    '.abo.pa',
    '.ac',
    '.ac.ae',
    '.ac.at',
    '.ac.be',
    '.ac.cn',
    '.ac.com',
    '.ac.cr',
    '.ac.cy',
    '.ac.fj',
    '.ac.fk',
    '.ac.gn',
    '.ac.id',
    '.ac.il',
    '.ac.im',
    '.ac.in',
    '.ac.ir',
    '.ac.jp',
    '.ac.mw',
    '.ac.nz',
    '.ac.pa',
    '.ac.ru',
    '.ac.rw',
    '.ac.se',
    '.ac.th',
    '.ac.tj',
    '.ac.tz',
    '.ac.ug',
    '.ac.uk',
    '.ac.vn',
    '.ac.yu',
    '.ac.za',
    '.ac.zm',
    '.ac.zw',
    '.ad',
    '.ad.jp',
    '.adm.br',
    '.adult.ht',
    '.adv.br',
    '.ae',
    '.aero',
    '.aero.mv',
    '.af',
    '.ag',
    '.agr.br',
    '.agrar.hu',
    '.ah.cn',
    '.ai',
    '.aichi.jp',
    '.ak.us',
    '.akita.jp',
    '.al',
    '.al.us',
    '.alt.za',
    '.am',
    '.am.br',
    '.an',
    '.ao',
    '.aomori.jp',
    '.aq',
    '.ar',
    '.ar.us',
    '.army.mil',
    '.arpa',
    '.arq.br',
    '.art.br',
    '.art.do',
    '.art.dz',
    '.art.ht',
    '.art.pl',
    '.as',
    '.asn.au',
    '.asn.lv',
    '.assn.lk',
    '.asso.dz',
    '.asso.fr',
    '.asso.ht',
    '.asso.mc',
    '.at',
    '.ato.br',
    '.au',
    '.av.tr',
    '.aw',
    '.az',
    '.az.us',
    '.ba',
    '.bb',
    '.bbs.tr',
    '.bc.ca',
    '.bd',
    '.bd.se',
    '.be',
    '.bel.tr',
    '.bf',
    '.bg',
    '.bh',
    '.bi',
    '.bialystok.pl',
    '.bio.br',
    '.biz',
    '.biz.cy',
    '.biz.et',
    '.biz.fj',
    '.biz.mv',
    '.biz.nr',
    '.biz.om',
    '.biz.pk',
    '.biz.pl',
    '.biz.pr',
    '.biz.tj',
    '.biz.tr',
    '.biz.tt',
    '.biz.vn',
    '.bj',
    '.bj.cn',
    '.bl.uk',
    '.bm',
    '.bmd.br',
    '.bn',
    '.bo',
    '.bolt.hu',
    '.br',
    '.bs',
    '.bt',
    '.bv',
    '.bw',
    '.by',
    '.bz',
    '.c.se',
    '.ca',
    '.ca',
    '.ca.us',
    '.casino.hu',
    '.cat',
    '.cc',
    '.cd',
    '.cd',
    '.cf',
    '.cg',
    '.ch',
    '.ch',
    '.cherkassy.ua',
    '.chernigov.ua',
    '.chernovtsy.ua',
    '.chiba.jp',
    '.ci',
    '.cim.br',
    '.city.hu',
    '.city.za',
    '.ck',
    '.ck.ua',
    '.cl',
    '.club.tw',
    '.cm',
    '.cn',
    '.cn',
    '.cn.ua',
    '.cng.br',
    '.cnt.br',
    '.co',
    '.co.ae',
    '.co.ag',
    '.co.at',
    '.co.bw',
    '.co.ck',
    '.co.cr',
    '.co.fk',
    '.co.gg',
    '.co.hu',
    '.co.id',
    '.co.il',
    '.co.im',
    '.co.in',
    '.co.ir',
    '.co.je',
    '.co.jp',
    '.co.kr',
    '.co.ls',
    '.co.ma',
    '.co.mu',
    '.co.mw',
    '.co.nz',
    '.co.om',
    '.co.rw',
    '.co.th',
    '.co.tj',
    '.co.tt',
    '.co.tz',
    '.co.ug',
    '.co.uk',
    '.co.us',
    '.co.ve',
    '.co.yu',
    '.co.za',
    '.co.zm',
    '.co.zw',
    '.com',
    '.com.ac',
    '.com.ag',
    '.com.ai',
    '.com.al',
    '.com.am',
    '.com.ar',
    '.com.au',
    '.com.aw',
    '.com.az',
    '.com.bb',
    '.com.bd',
    '.com.bm',
    '.com.bn',
    '.com.bo',
    '.com.br',
    '.com.bs',
    '.com.bt',
    '.com.cd',
    '.com.ch',
    '.com.cn',
    '.com.co',
    '.com.cu',
    '.com.cy',
    '.com.dm',
    '.com.do',
    '.com.dz',
    '.com.ec',
    '.com.ee',
    '.com.eg',
    '.com.es',
    '.com.et',
    '.com.fj',
    '.com.fr',
    '.com.ge',
    '.com.gh',
    '.com.gi',
    '.com.gn',
    '.com.gr',
    '.com.hk',
    '.com.hn',
    '.com.hr',
    '.com.ht',
    '.com.jm',
    '.com.jo',
    '.com.kh',
    '.com.kw',
    '.com.ky',
    '.com.kz',
    '.com.lb',
    '.com.lc',
    '.com.li',
    '.com.lk',
    '.com.lr',
    '.com.lv',
    '.com.ly',
    '.com.mg',
    '.com.mk',
    '.com.mo',
    '.com.mt',
    '.com.mu',
    '.com.mv',
    '.com.mw',
    '.com.mx',
    '.com.my',
    '.com.ng',
    '.com.ni',
    '.com.np',
    '.com.nr',
    '.com.om',
    '.com.pa',
    '.com.pe',
    '.com.pf',
    '.com.pg',
    '.com.ph',
    '.com.pk',
    '.com.pl',
    '.com.pr',
    '.com.ps',
    '.com.pt',
    '.com.py',
    '.com.ru',
    '.com.rw',
    '.com.sa',
    '.com.sb',
    '.com.sc',
    '.com.sd',
    '.com.sg',
    '.com.sv',
    '.com.sy',
    '.com.tj',
    '.com.tn',
    '.com.tr',
    '.com.tt',
    '.com.tw',
    '.com.ua',
    '.com.uy',
    '.com.ve',
    '.com.vi',
    '.com.vn',
    '.com.ye',
    '.conf.lv',
    '.coop',
    '.coop.br',
    '.coop.ht',
    '.coop.mv',
    '.coop.mw',
    '.cpa.pro',
    '.cq.cn',
    '.cr',
    '.cri.nz',
    '.crimea.ua',
    '.csiro.au',
    '.ct.us',
    '.cu',
    '.cu',
    '.cv',
    '.cv.ua',
    '.cx',
    '.cx',
    '.cy',
    '.cz',
    '.d.se',
    '.dc.us',
    '.de',
    '.de.us',
    '.dj',
    '.dk',
    '.dm',
    '.dm',
    '.dn.ua',
    '.dnepropetrovsk.ua',
    '.dni.us',
    '.do',
    '.donetsk.ua',
    '.dp.ua',
    '.dpn.br',
    '.dr.tr',
    '.dz',
    '.dz',
    '.e.se',
    '.e164.arpa',
    '.ebiz.tw',
    '.ec',
    '.ec',
    '.ecn.br',
    '.ed.cr',
    '.ed.jp',
    '.edu',
    '.edu.ac',
    '.edu.al',
    '.edu.au',
    '.edu.bb',
    '.edu.bd',
    '.edu.bm',
    '.edu.bn',
    '.edu.bo',
    '.edu.br',
    '.edu.bt',
    '.edu.cn',
    '.edu.co',
    '.edu.cu',
    '.edu.dm',
    '.edu.do',
    '.edu.dz',
    '.edu.ec',
    '.edu.eg',
    '.edu.es',
    '.edu.et',
    '.edu.ge',
    '.edu.gh',
    '.edu.gi',
    '.edu.gr',
    '.edu.hk',
    '.edu.hn',
    '.edu.ht',
    '.edu.in',
    '.edu.jm',
    '.edu.jo',
    '.edu.kh',
    '.edu.kw',
    '.edu.ky',
    '.edu.kz',
    '.edu.lb',
    '.edu.lc',
    '.edu.lk',
    '.edu.lr',
    '.edu.lv',
    '.edu.ly',
    '.edu.mg',
    '.edu.mo',
    '.edu.mt',
    '.edu.mv',
    '.edu.mw',
    '.edu.mx',
    '.edu.my',
    '.edu.ng',
    '.edu.ni',
    '.edu.np',
    '.edu.nr',
    '.edu.om',
    '.edu.pa',
    '.edu.pe',
    '.edu.pf',
    '.edu.pk',
    '.edu.pl',
    '.edu.pr',
    '.edu.ps',
    '.edu.pt',
    '.edu.py',
    '.edu.rw',
    '.edu.sa',
    '.edu.sb',
    '.edu.sc',
    '.edu.sd',
    '.edu.sg',
    '.edu.sv',
    '.edu.tj',
    '.edu.tr',
    '.edu.tt',
    '.edu.tw',
    '.edu.ua',
    '.edu.uy',
    '.edu.vi',
    '.edu.vn',
    '.edu.yu',
    '.edu.za',
    '.ee',
    '.ee',
    '.eg',
    '.ehime.jp',
    '.ekloges.cy',
    '.eng.br',
    '.ens.tn',
    '.er',
    '.erotica.hu',
    '.erotika.hu',
    '.es',
    '.es',
    '.esp.br',
    '.et',
    '.etc.br',
    '.eti.br',
    '.eu',
    '.eun.eg',
    '.f.se',
    '.fam.pk',
    '.far.br',
    '.fed.us',
    '.fhs.no',
    '.fi',
    '.fi.cr',
    '.fie.ee',
    '.film.hu',
    '.fin.ec',
    '.fin.tn',
    '.firm.ht',
    '.firm.in',
    '.fj',
    '.fj.cn',
    '.fk',
    '.fl.us',
    '.fm',
    '.fm.br',
    '.fnd.br',
    '.fo',
    '.folkebibl.no',
    '.forum.hu',
    '.fot.br',
    '.fr',
    '.fr',
    '.from.hr',
    '.fst.br',
    '.fukui.jp',
    '.fukuoka.jp',
    '.fukushima.jp',
    '.fylkesbibl.no',
    '.g.se',
    '.g12.br',
    '.ga',
    '.ga.us',
    '.game.tw',
    '.games.hu',
    '.gb',
    '.gd',
    '.gd.cn',
    '.gda.pl',
    '.gdansk.pl',
    '.ge',
    '.ge',
    '.geek.nz',
    '.gen.in',
    '.gen.nz',
    '.gen.tr',
    '.gf',
    '.gg',
    '.gg',
    '.ggf.br',
    '.gh',
    '.gi',
    '.gi',
    '.gifu.jp',
    '.gl',
    '.gm',
    '.go.cr',
    '.go.id',
    '.go.jp',
    '.go.th',
    '.go.tj',
    '.go.tz',
    '.go.ug',
    '.gob.bo',
    '.gob.do',
    '.gob.es',
    '.gob.hn',
    '.gob.mx',
    '.gob.ni',
    '.gob.pa',
    '.gob.pe',
    '.gob.pk',
    '.gob.sv',
    '.gok.pk',
    '.gon.pk',
    '.gop.pk',
    '.gos.pk',
    '.gouv.fr',
    '.gouv.ht',
    '.gouv.rw',
    '.gov',
    '.gov.ac',
    '.gov.ae',
    '.gov.al',
    '.gov.au',
    '.gov.bb',
    '.gov.bd',
    '.gov.bf',
    '.gov.bm',
    '.gov.bo',
    '.gov.br',
    '.gov.bt',
    '.gov.by',
    '.gov.ch',
    '.gov.cn',
    '.gov.co',
    '.gov.cu',
    '.gov.cx',
    '.gov.dm',
    '.gov.do',
    '.gov.dz',
    '.gov.ec',
    '.gov.eg',
    '.gov.et',
    '.gov.fj',
    '.gov.fk',
    '.gov.ge',
    '.gov.gh',
    '.gov.gi',
    '.gov.gn',
    '.gov.gr',
    '.gov.hk',
    '.gov.ie',
    '.gov.il',
    '.gov.im',
    '.gov.in',
    '.gov.ir',
    '.gov.it',
    '.gov.jm',
    '.gov.jo',
    '.gov.kh',
    '.gov.kw',
    '.gov.ky',
    '.gov.kz',
    '.gov.lb',
    '.gov.lc',
    '.gov.li',
    '.gov.lk',
    '.gov.lr',
    '.gov.lt',
    '.gov.lu',
    '.gov.lv',
    '.gov.ly',
    '.gov.ma',
    '.gov.mg',
    '.gov.mo',
    '.gov.mt',
    '.gov.mv',
    '.gov.mw',
    '.gov.my',
    '.gov.ng',
    '.gov.np',
    '.gov.nr',
    '.gov.om',
    '.gov.ph',
    '.gov.pk',
    '.gov.pl',
    '.gov.pr',
    '.gov.ps',
    '.gov.pt',
    '.gov.py',
    '.gov.rw',
    '.gov.sa',
    '.gov.sb',
    '.gov.sc',
    '.gov.sd',
    '.gov.sg',
    '.gov.sy',
    '.gov.tj',
    '.gov.tn',
    '.gov.to',
    '.gov.tp',
    '.gov.tr',
    '.gov.tt',
    '.gov.tv',
    '.gov.tw',
    '.gov.ua',
    '.gov.uk',
    '.gov.vi',
    '.gov.vn',
    '.gov.za',
    '.gov.zm',
    '.gov.zw',
    '.govt.nz',
    '.gp',
    '.gq',
    '.gr',
    '.gr',
    '.gr.jp',
    '.grp.lk',
    '.gs',
    '.gs.cn',
    '.gt',
    '.gu',
    '.gub.uy',
    '.gunma.jp',
    '.gv.at',
    '.gw',
    '.gx.cn',
    '.gy',
    '.gz.cn',
    '.h.se',
    '.ha.cn',
    '.hb.cn',
    '.he.cn',
    '.health.vn',
    '.herad.no',
    '.hi.cn',
    '.hi.us',
    '.hiroshima.jp',
    '.hk',
    '.hk',
    '.hl.cn',
    '.hm',
    '.hn',
    '.hn',
    '.hn.cn',
    '.hokkaido.jp',
    '.hotel.hu',
    '.hotel.lk',
    '.hr',
    '.hr',
    '.ht',
    '.ht',
    '.hu',
    '.hu',
    '.hyogo.jp',
    '.i.se',
    '.ia.us',
    '.ibaraki.jp',
    '.icnet.uk',
    '.id',
    '.id.au',
    '.id.lv',
    '.id.ly',
    '.id.us',
    '.idf.il',
    '.idn.sg',
    '.idrett.no',
    '.idv.hk',
    '.idv.tw',
    '.ie',
    '.ie',
    '.if.ua',
    '.il',
    '.il.us',
    '.im',
    '.imb.br',
    '.in',
    '.in',
    '.in.th',
    '.in.us',
    '.ind.br',
    '.ind.in',
    '.ind.tn',
    '.inf.br',
    '.inf.cu',
    '.info',
    '.info.cy',
    '.info.ec',
    '.info.et',
    '.info.fj',
    '.info.ht',
    '.info.hu',
    '.info.mv',
    '.info.nr',
    '.info.pl',
    '.info.pr',
    '.info.sd',
    '.info.tn',
    '.info.tr',
    '.info.tt',
    '.info.ve',
    '.info.vn',
    '.ing.pa',
    '.ingatlan.hu',
    '.int',
    '.int.bo',
    '.int.lk',
    '.int.mv',
    '.int.mw',
    '.int.pt',
    '.int.ru',
    '.int.rw',
    '.int.tj',
    '.int.vn',
    '.intl.tn',
    '.io',
    '.ip6.arpa',
    '.iq',
    '.ir',
    '.ir',
    '.is',
    '.isa.us',
    '.ishikawa.jp',
    '.isla.pr',
    '.it',
    '.it',
    '.iwate.jp',
    '.iwi.nz',
    '.iz.hr',
    '.je',
    '.je',
    '.jet.uk',
    '.jl.cn',
    '.jm',
    '.jo',
    '.jo',
    '.jobs',
    '.jogasz.hu',
    '.jor.br',
    '.jp',
    '.jp',
    '.js.cn',
    '.jx.cn',
    '.k.se',
    '.k12.il',
    '.k12.tr',
    '.kagawa.jp',
    '.kagoshima.jp',
    '.kanagawa.jp',
    '.kawasaki.jp',
    '.ke',
    '.kg',
    '.kh',
    '.kh.ua',
    '.kharkov.ua',
    '.kherson.ua',
    '.khmelnitskiy.ua',
    '.ki',
    '.kids.us',
    '.kiev.ua',
    '.kirovograd.ua',
    '.kitakyushu.jp',
    '.km',
    '.km.ua',
    '.kn',
    '.kobe.jp',
    '.kochi.jp',
    '.kommune.no',
    '.konyvelo.hu',
    '.kr',
    '.kr',
    '.kr.ua',
    '.krakow.pl',
    '.ks.ua',
    '.ks.us',
    '.kumamoto.jp',
    '.kv.ua',
    '.kw',
    '.ky',
    '.ky',
    '.ky.us',
    '.kyoto.jp',
    '.kz',
    '.la',
    '.la.us',
    '.lakas.hu',
    '.law.pro',
    '.law.za',
    '.lb',
    '.lc',
    '.lel.br',
    '.lg.jp',
    '.lg.ua',
    '.li',
    '.li',
    '.lk',
    '.lk',
    '.ln.cn',
    '.lodz.pl',
    '.lr',
    '.ls',
    '.lt',
    '.lt',
    '.ltd.cy',
    '.ltd.gi',
    '.ltd.lk',
    '.ltd.uk',
    '.lu',
    '.lu',
    '.lublin.pl',
    '.lugansk.ua',
    '.lutsk.ua',
    '.lv',
    '.lv',
    '.lviv.ua',
    '.ly',
    '.ly',
    '.m.se',
    '.ma',
    '.ma',
    '.ma.us',
    '.maori.nz',
    '.mat.br',
    '.mb.ca',
    '.mc',
    '.mc',
    '.md',
    '.md.us',
    '.me.uk',
    '.me.us',
    '.med.br',
    '.med.ec',
    '.med.ht',
    '.med.ly',
    '.med.om',
    '.med.pa',
    '.med.pro',
    '.med.sa',
    '.med.sd',
    '.media.hu',
    '.mg',
    '.mg',
    '.mh',
    '.mi.th',
    '.mi.us',
    '.mie.jp',
    '.mil',
    '.mil.ac',
    '.mil.ae',
    '.mil.be',
    '.mil.bo',
    '.mil.br',
    '.mil.by',
    '.mil.co',
    '.mil.do',
    '.mil.ec',
    '.mil.eg',
    '.mil.fj',
    '.mil.ge',
    '.mil.gh',
    '.mil.hn',
    '.mil.in',
    '.mil.jo',
    '.mil.kh',
    '.mil.kw',
    '.mil.kz',
    '.mil.lt',
    '.mil.lu',
    '.mil.lv',
    '.mil.mg',
    '.mil.mv',
    '.mil.my',
    '.mil.no',
    '.mil.np',
    '.mil.nz',
    '.mil.om',
    '.mil.pe',
    '.mil.pl',
    '.mil.rw',
    '.mil.tj',
    '.mil.tr',
    '.mil.tw',
    '.mil.uk',
    '.mil.uy',
    '.mil.za',
    '.miyagi.jp',
    '.miyazaki.jp',
    '.mk',
    '.mk',
    '.mk.ua',
    '.ml',
    '.mm',
    '.mn',
    '.mn.us',
    '.mo',
    '.mo',
    '.mo.us',
    '.mobi',
    '.mod.gi',
    '.mod.uk',
    '.mp',
    '.mq',
    '.mr',
    '.ms',
    '.ms.us',
    '.msk.ru',
    '.mt',
    '.mt',
    '.mt.us',
    '.mu',
    '.mu',
    '.muni.il',
    '.mus.br',
    '.museum',
    '.museum.mv',
    '.museum.mw',
    '.museum.no',
    '.museum.om',
    '.music.mobi',
    '.mv',
    '.mw',
    '.n.se',
    '.na',
    '.nagano.jp',
    '.nagasaki.jp',
    '.nagoya.jp',
    '.name',
    '.name.ae',
    '.name.cy',
    '.name.et',
    '.name.fj',
    '.name.hr',
    '.name.mv',
    '.name.my',
    '.name.pr',
    '.name.tj',
    '.name.tr',
    '.name.tt',
    '.name.vn',
    '.nara.jp',
    '.nat.tn',
    '.navy.mil',
    '.nb.ca',
    '.nc',
    '.nc.us',
    '.nd.us',
    '.ne',
    '.ne.jp',
    '.ne.tz',
    '.ne.ug',
    '.ne.us',
    '.nel.uk',
    '.net',
    '.net.ac',
    '.net.ae',
    '.net.ag',
    '.net.ai',
    '.net.al',
    '.net.am',
    '.net.ar',
    '.net.au',
    '.net.az',
    '.net.bb',
    '.net.bd',
    '.net.bm',
    '.net.bn',
    '.net.bo',
    '.net.br',
    '.net.bs',
    '.net.bt',
    '.net.cd',
    '.net.ch',
    '.net.cn',
    '.net.co',
    '.net.cu',
    '.net.cy',
    '.net.dm',
    '.net.do',
    '.net.dz',
    '.net.ec',
    '.net.eg',
    '.net.et',
    '.net.fj',
    '.net.fk',
    '.net.ge',
    '.net.gg',
    '.net.gn',
    '.net.gr',
    '.net.hk',
    '.net.hn',
    '.net.ht',
    '.net.il',
    '.net.im',
    '.net.in',
    '.net.ir',
    '.net.je',
    '.net.jm',
    '.net.jo',
    '.net.kh',
    '.net.kw',
    '.net.ky',
    '.net.kz',
    '.net.lb',
    '.net.li',
    '.net.lk',
    '.net.lr',
    '.net.lu',
    '.net.lv',
    '.net.ly',
    '.net.ma',
    '.net.mo',
    '.net.mt',
    '.net.mv',
    '.net.mw',
    '.net.mx',
    '.net.my',
    '.net.ng',
    '.net.ni',
    '.net.np',
    '.net.nr',
    '.net.nz',
    '.net.om',
    '.net.pa',
    '.net.pe',
    '.net.pg',
    '.net.pk',
    '.net.pl',
    '.net.pr',
    '.net.ps',
    '.net.pt',
    '.net.py',
    '.net.ru',
    '.net.rw',
    '.net.sa',
    '.net.sb',
    '.net.sc',
    '.net.sd',
    '.net.sg',
    '.net.sy',
    '.net.th',
    '.net.tj',
    '.net.tn',
    '.net.tr',
    '.net.tt',
    '.net.tw',
    '.net.ua',
    '.net.uk',
    '.net.uy',
    '.net.ve',
    '.net.vn',
    '.net.ye',
    '.net.za',
    '.news.hu',
    '.nf',
    '.nf.ca',
    '.ng',
    '.ngo.lk',
    '.ngo.pl',
    '.ngo.za',
    '.nh.us',
    '.nhs.uk',
    '.ni',
    '.nic.im',
    '.nic.in',
    '.nic.uk',
    '.niigata.jp',
    '.nikolaev.ua',
    '.nj.us',
    '.nl',
    '.nl',
    '.nl.ca',
    '.nls.uk',
    '.nm.cn',
    '.nm.us',
    '.no',
    '.no',
    '.nom.ad',
    '.nom.ag',
    '.nom.br',
    '.nom.co',
    '.nom.es',
    '.nom.fk',
    '.nom.fr',
    '.nom.mg',
    '.nom.ni',
    '.nom.pa',
    '.nom.pe',
    '.nom.za',
    '.nome.pt',
    '.not.br',
    '.np',
    '.nr',
    '.nr',
    '.nr',
    '.ns.ca',
    '.nsn.us',
    '.nt.ca',
    '.ntr.br',
    '.nu',
    '.nu.ca',
    '.nv.us',
    '.nx.cn',
    '.ny.us',
    '.nz',
    '.o.se',
    '.od.ua',
    '.odessa.ua',
    '.odo.br',
    '.off.ai',
    '.oh.us',
    '.oita.jp',
    '.ok.us',
    '.okayama.jp',
    '.okinawa.jp',
    '.olsztyn.pl',
    '.om',
    '.on.ca',
    '.or.at',
    '.or.cr',
    '.or.id',
    '.or.jp',
    '.or.kr',
    '.or.th',
    '.or.tz',
    '.or.ug',
    '.or.us',
    '.org',
    '.org.ac',
    '.org.ae',
    '.org.ag',
    '.org.ai',
    '.org.al',
    '.org.am',
    '.org.ar',
    '.org.au',
    '.org.az',
    '.org.bb',
    '.org.bd',
    '.org.bm',
    '.org.bn',
    '.org.bo',
    '.org.br',
    '.org.bs',
    '.org.bt',
    '.org.bw',
    '.org.cd',
    '.org.ch',
    '.org.cn',
    '.org.co',
    '.org.cu',
    '.org.cy',
    '.org.dm',
    '.org.do',
    '.org.dz',
    '.org.ec',
    '.org.ee',
    '.org.eg',
    '.org.es',
    '.org.et',
    '.org.fj',
    '.org.fk',
    '.org.ge',
    '.org.gg',
    '.org.gh',
    '.org.gi',
    '.org.gn',
    '.org.gr',
    '.org.hk',
    '.org.hn',
    '.org.ht',
    '.org.hu',
    '.org.il',
    '.org.im',
    '.org.in',
    '.org.ir',
    '.org.je',
    '.org.jm',
    '.org.jo',
    '.org.kh',
    '.org.kw',
    '.org.ky',
    '.org.kz',
    '.org.lb',
    '.org.lc',
    '.org.li',
    '.org.lk',
    '.org.lr',
    '.org.ls',
    '.org.lu',
    '.org.lv',
    '.org.ly',
    '.org.ma',
    '.org.mg',
    '.org.mk',
    '.org.mo',
    '.org.mt',
    '.org.mv',
    '.org.mw',
    '.org.mx',
    '.org.my',
    '.org.ng',
    '.org.ni',
    '.org.np',
    '.org.nr',
    '.org.nz',
    '.org.om',
    '.org.pa',
    '.org.pe',
    '.org.pf',
    '.org.pk',
    '.org.pl',
    '.org.pr',
    '.org.ps',
    '.org.pt',
    '.org.py',
    '.org.ru',
    '.org.sa',
    '.org.sc',
    '.org.sd',
    '.org.se',
    '.org.sg',
    '.org.sv',
    '.org.tj',
    '.org.tn',
    '.org.tr',
    '.org.tt',
    '.org.tw',
    '.org.ua',
    '.org.uk',
    '.org.uy',
    '.org.ve',
    '.org.vi',
    '.org.vn',
    '.org.yu',
    '.org.za',
    '.org.zm',
    '.org.zw',
    '.osaka.jp',
    '.pa',
    '.pa.us',
    '.parliament.cy',
    '.parliament.uk',
    '.parti.se',
    '.pe',
    '.pe.ca',
    '.per.kh',
    '.per.sg',
    '.perso.ht',
    '.pf',
    '.pf',
    '.pg',
    '.ph',
    '.ph',
    '.pk',
    '.pk',
    '.pl',
    '.pl',
    '.pl.ua',
    '.plc.ly',
    '.plc.uk',
    '.plo.ps',
    '.pm',
    '.pn',
    '.pol.dz',
    '.pol.ht',
    '.pol.tr',
    '.police.uk',
    '.poltava.ua',
    '.post',
    '.poznan.pl',
    '.pp.ru',
    '.pp.se',
    '.ppg.br',
    '.pr',
    '.pr',
    '.prd.fr',
    '.prd.mg',
    '.press.cy',
    '.press.se',
    '.presse.fr',
    '.pri.ee',
    '.priv.hu',
    '.priv.no',
    '.pro',
    '.pro.ae',
    '.pro.br',
    '.pro.cy',
    '.pro.ec',
    '.pro.fj',
    '.pro.ht',
    '.pro.mv',
    '.pro.om',
    '.pro.pr',
    '.pro.tt',
    '.pro.vn',
    '.ps',
    '.ps',
    '.psc.br',
    '.psi.br',
    '.pt',
    '.pt',
    '.pub.sa',
    '.publ.pt',
    '.pvt.ge',
    '.pw',
    '.py',
    '.qa',
    '.qc.ca',
    '.qh.cn',
    '.qsl.br',
    '.re',
    '.rec.br',
    '.red.sv',
    '.reklam.hu',
    '.rel.ht',
    '.res.in',
    '.ri.us',
    '.ro',
    '.ro',
    '.rovno.ua',
    '.ru',
    '.ru',
    '.rv.ua',
    '.rw',
    '.rw',
    '.s.se',
    '.sa',
    '.sa.cr',
    '.saga.jp',
    '.saitama.jp',
    '.sapporo.jp',
    '.sb',
    '.sc',
    '.sc',
    '.sc.cn',
    '.sc.ug',
    '.sc.us',
    '.sch.ae',
    '.sch.ir',
    '.sch.lk',
    '.sch.ly',
    '.sch.om',
    '.sch.sa',
    '.sch.uk',
    '.sch.zm',
    '.school.fj',
    '.school.nz',
    '.school.za',
    '.sci.eg',
    '.sd',
    '.sd',
    '.sd.cn',
    '.sd.us',
    '.se',
    '.se',
    '.sebastopol.ua',
    '.sec.ps',
    '.sendai.jp',
    '.sex.hu',
    '.sg',
    '.sg',
    '.sh',
    '.sh.cn',
    '.shiga.jp',
    '.shimane.jp',
    '.shizuoka.jp',
    '.shop.ht',
    '.shop.hu',
    '.si',
    '.sj',
    '.sk',
    '.sk.ca',
    '.sl',
    '.sld.do',
    '.sld.pa',
    '.slg.br',
    '.slupsk.pl',
    '.sm',
    '.sn',
    '.sn.cn',
    '.so',
    '.soc.lk',
    '.sport.hu',
    '.sr',
    '.srv.br',
    '.st',
    '.stat.no',
    '.su',
    '.suli.hu',
    '.sumy.ua',
    '.sv',
    '.sx.cn',
    '.sy',
    '.sz',
    '.szczecin.pl',
    '.szex.hu',
    '.t.se',
    '.tc',
    '.td',
    '.te.ua',
    '.tel.tr',
    '.ternopil.ua',
    '.tf',
    '.tg',
    '.th',
    '.tj',
    '.tj',
    '.tj.cn',
    '.tk',
    '.tl',
    '.tm',
    '.tm.cy',
    '.tm.fr',
    '.tm.hu',
    '.tm.mc',
    '.tm.mg',
    '.tm.se',
    '.tm.za',
    '.tmp.br',
    '.tn',
    '.tn.us',
    '.to',
    '.to',
    '.to',
    '.tochigi.jp',
    '.tokushima.jp',
    '.tokyo.jp',
    '.torun.pl',
    '.tottori.jp',
    '.tourism.tn',
    '.toyama.jp',
    '.tozsde.hu',
    '.tp',
    '.tr',
    '.travel',
    '.trd.br',
    '.tt',
    '.tt',
    '.tur.br',
    '.tv',
    '.tv',
    '.tv.bo',
    '.tv.br',
    '.tv.sd',
    '.tw',
    '.tw',
    '.tw',
    '.tw',
    '.tw',
    '.tx.us',
    '.tz',
    '.u.se',
    '.ua',
    '.ua',
    '.ug',
    '.ug',
    '.uk',
    '.um',
    '.uri.arpa',
    '.urn.arpa',
    '.us',
    '.us',
    '.ut.us',
    '.utazas.hu',
    '.uy',
    '.uz',
    '.uzhgorod.ua',
    '.va',
    '.va.us',
    '.vatican.va',
    '.vc',
    '.ve',
    '.vet.br',
    '.vg',
    '.vgs.no',
    '.vi',
    '.vi',
    '.video.hu',
    '.vinnica.ua',
    '.vn',
    '.vn',
    '.vn.ua',
    '.vt.us',
    '.vuwf',
    '.w.se',
    '.wa.us',
    '.wakayama.jp',
    '.warszawa.pl',
    '.waw.pl',
    '.weather.mobi',
    '.web.do',
    '.web.lk',
    '.web.pk',
    '.web.tj',
    '.web.tr',
    '.web.ve',
    '.web.za',
    '.wi.us',
    '.wroc.pl',
    '.wroclaw.pl',
    '.wv.us',
    '.wy.us',
    '.x.se',
    '.xj.cn',
    '.xz.cn',
    '.y.se',
    '.yamagata.jp',
    '.yamaguchi.jp',
    '.yamanashi.jp',
    '.ye',
    '.yk.ca',
    '.yn.cn',
    '.yokohama.jp',
    '.yt',
    '.yu',
    '.z.se',
    '.za',
    '.zaporizhzhe.ua',
    '.zhitomir.ua',
    '.zj.cn',
    '.zlg.br',
    '.zm',
    '.zp.ua',
    '.zt.ua',
    '.zw'
))




if __name__=="__main__":
    for item in ['http://something.unknown','http://a.b.c.something.unknown','http://something','http://google.com','http://a.b.c.d.e.google.com','http://something.uk','http://aa.bb.cc.dd.ee.ff.gg.guardian.co.uk','http://guardian.co.uk','http://www.guardian.co.uk','http://www.google.com','http://wikipedia.org','http://www.wikipedia.org','',None,'whatever']:
        for level in range(0,5):
            print "url=%s, levels=%s => %s" % (item, level, parse_domain(item,level))
