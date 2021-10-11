function navigateByHash(){
    const hash = window.location.hash;
      hash && $('ul.nav.nav-tabs a[href="' + hash + '"]').tab('show');
      $('ul.nav.nav-tabs a').click(function (e) {
         $(this).tab('show');
         $('body').scrollTop();
         window.location.hash = this.hash;
      });
}

$(window).on('hashchange', navigateByHash);
$(window).on('load', navigateByHash);
