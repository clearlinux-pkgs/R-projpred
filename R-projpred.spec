#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-projpred
Version  : 2.2.1
Release  : 22
URL      : https://cran.r-project.org/src/contrib/projpred_2.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/projpred_2.2.1.tar.gz
Summary  : Projection Predictive Feature Selection
Group    : Development/Tools
License  : GPL-3.0
Requires: R-projpred-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-dplyr
Requires: R-gamm4
Requires: R-ggplot2
Requires: R-lme4
Requires: R-loo
Requires: R-magrittr
Requires: R-mvtnorm
Requires: R-rlang
Requires: R-rstantools
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-dplyr
BuildRequires : R-gamm4
BuildRequires : R-ggplot2
BuildRequires : R-lme4
BuildRequires : R-loo
BuildRequires : R-magrittr
BuildRequires : R-mvtnorm
BuildRequires : R-rlang
BuildRequires : R-rstantools
BuildRequires : buildreq-R

%description
Performs projection predictive feature selection for generalized linear and
    additive models as well as for generalized linear and additive multilevel
    models (see Piironen, Paasiniemi and Vehtari, 2020,

%package lib
Summary: lib components for the R-projpred package.
Group: Libraries

%description lib
lib components for the R-projpred package.


%prep
%setup -q -n projpred
cd %{_builddir}/projpred

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663691916

%install
export SOURCE_DATE_EPOCH=1663691916
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/projpred/CITATION
/usr/lib64/R/library/projpred/DESCRIPTION
/usr/lib64/R/library/projpred/INDEX
/usr/lib64/R/library/projpred/LICENSE
/usr/lib64/R/library/projpred/Meta/Rd.rds
/usr/lib64/R/library/projpred/Meta/data.rds
/usr/lib64/R/library/projpred/Meta/features.rds
/usr/lib64/R/library/projpred/Meta/hsearch.rds
/usr/lib64/R/library/projpred/Meta/links.rds
/usr/lib64/R/library/projpred/Meta/nsInfo.rds
/usr/lib64/R/library/projpred/Meta/package.rds
/usr/lib64/R/library/projpred/Meta/vignette.rds
/usr/lib64/R/library/projpred/NAMESPACE
/usr/lib64/R/library/projpred/NEWS.md
/usr/lib64/R/library/projpred/R/projpred
/usr/lib64/R/library/projpred/R/projpred.rdb
/usr/lib64/R/library/projpred/R/projpred.rdx
/usr/lib64/R/library/projpred/data/Rdata.rdb
/usr/lib64/R/library/projpred/data/Rdata.rds
/usr/lib64/R/library/projpred/data/Rdata.rdx
/usr/lib64/R/library/projpred/doc/index.html
/usr/lib64/R/library/projpred/doc/projpred.R
/usr/lib64/R/library/projpred/doc/projpred.Rmd
/usr/lib64/R/library/projpred/doc/projpred.html
/usr/lib64/R/library/projpred/help/AnIndex
/usr/lib64/R/library/projpred/help/aliases.rds
/usr/lib64/R/library/projpred/help/figures/logo.svg
/usr/lib64/R/library/projpred/help/paths.rds
/usr/lib64/R/library/projpred/help/projpred.rdb
/usr/lib64/R/library/projpred/help/projpred.rdx
/usr/lib64/R/library/projpred/html/00Index.html
/usr/lib64/R/library/projpred/html/R.css
/usr/lib64/R/library/projpred/tests/testthat.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/args.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/formul_handlers.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/getters.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/revIA.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/testers.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/unlist_cust.R
/usr/lib64/R/library/projpred/tests/testthat/setup.R
/usr/lib64/R/library/projpred/tests/testthat/test_as_matrix.R
/usr/lib64/R/library/projpred/tests/testthat/test_cvindices.R
/usr/lib64/R/library/projpred/tests/testthat/test_datafit.R
/usr/lib64/R/library/projpred/tests/testthat/test_div_minimizer.R
/usr/lib64/R/library/projpred/tests/testthat/test_extend_family.R
/usr/lib64/R/library/projpred/tests/testthat/test_formula.R
/usr/lib64/R/library/projpred/tests/testthat/test_glm_elnet.R
/usr/lib64/R/library/projpred/tests/testthat/test_glm_ridge.R
/usr/lib64/R/library/projpred/tests/testthat/test_latent.R
/usr/lib64/R/library/projpred/tests/testthat/test_methods_vsel.R
/usr/lib64/R/library/projpred/tests/testthat/test_misc.R
/usr/lib64/R/library/projpred/tests/testthat/test_parallel.R
/usr/lib64/R/library/projpred/tests/testthat/test_proj_pred.R
/usr/lib64/R/library/projpred/tests/testthat/test_proj_predfun.R
/usr/lib64/R/library/projpred/tests/testthat/test_project.R
/usr/lib64/R/library/projpred/tests/testthat/test_refmodel.R
/usr/lib64/R/library/projpred/tests/testthat/test_varsel.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/projpred/libs/projpred.so
/usr/lib64/R/library/projpred/libs/projpred.so.avx2
/usr/lib64/R/library/projpred/libs/projpred.so.avx512
