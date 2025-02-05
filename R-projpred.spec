#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-projpred
Version  : 2.8.0
Release  : 36
URL      : https://cran.r-project.org/src/contrib/projpred_2.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/projpred_2.8.0.tar.gz
Summary  : Projection Predictive Feature Selection
Group    : Development/Tools
License  : GPL-3.0
Requires: R-projpred-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-abind
Requires: R-gamm4
Requires: R-ggplot2
Requires: R-gtools
Requires: R-lme4
Requires: R-loo
Requires: R-mclogit
Requires: R-mvtnorm
Requires: R-ordinal
Requires: R-rstantools
Requires: R-scales
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-RcppArmadillo-dev
BuildRequires : R-abind
BuildRequires : R-gamm4
BuildRequires : R-ggplot2
BuildRequires : R-gtools
BuildRequires : R-lme4
BuildRequires : R-loo
BuildRequires : R-mclogit
BuildRequires : R-mvtnorm
BuildRequires : R-ordinal
BuildRequires : R-rstantools
BuildRequires : R-scales
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Performs projection predictive feature selection for generalized linear

%package lib
Summary: lib components for the R-projpred package.
Group: Libraries

%description lib
lib components for the R-projpred package.


%prep
%setup -q -n projpred
pushd ..
cp -a projpred buildavx2
popd
pushd ..
cp -a projpred buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737153927

%install
export SOURCE_DATE_EPOCH=1737153927
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/projpred/doc/latent.R
/usr/lib64/R/library/projpred/doc/latent.Rmd
/usr/lib64/R/library/projpred/doc/latent.html
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
/usr/lib64/R/library/projpred/tests/testthat/helpers/dummies.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/formul_handlers.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/getters.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/predictor_handlers.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/testers.R
/usr/lib64/R/library/projpred/tests/testthat/helpers/unlist_cust.R
/usr/lib64/R/library/projpred/tests/testthat/setup.R
/usr/lib64/R/library/projpred/tests/testthat/test_as_matrix.R
/usr/lib64/R/library/projpred/tests/testthat/test_augdat.R
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
/V3/usr/lib64/R/library/projpred/libs/projpred.so
/V4/usr/lib64/R/library/projpred/libs/projpred.so
/usr/lib64/R/library/projpred/libs/projpred.so
